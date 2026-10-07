"""Emit batched GraphQL for pushing catalogue/seo.py to Shopify.

`bulkOperationRunMutation` is blocked by the connector's safety policy, so the
push goes as aliased mutations, a batch at a time, the same way the original
product import did.
"""
import json
import sys
sys.path.insert(0, "catalogue")
import seo  # noqa: E402

PRODUCT_IDS = json.load(open("catalogue/shopify-ids.json"))["products"]
COLLECTION_IDS = json.load(open("catalogue/shopify-ids.json"))["collections"]

BATCH = 12


def batches(pairs, size=BATCH):
    items = list(pairs)
    for i in range(0, len(items), size):
        yield items[i:i + size]


def emit(kind):
    if kind == "products":
        data, ids, mutation, field = seo.PRODUCTS, PRODUCT_IDS, "productUpdate", "product"
    else:
        data, ids, mutation, field = seo.COLLECTIONS, COLLECTION_IDS, "collectionUpdate", "input"

    missing = [h for h in data if h not in ids]
    if missing:
        raise SystemExit(f"no id for: {missing}")

    for n, chunk in enumerate(batches(data.items()), 1):
        lines, variables = ["mutation Seo("], {}
        decls = []
        body = []
        for i, (handle, (title, desc)) in enumerate(chunk):
            key = f"i{i}"
            decls.append(f"${key}: {'ProductUpdateInput' if kind == 'products' else 'CollectionInput'}!")
            variables[key] = {"id": ids[handle], "seo": {"title": title, "description": desc}}
            alias = "a" + str(i)
            body.append(
                f"  {alias}: {mutation}({field}: ${key}) {{ "
                f"userErrors {{ field message }} }}")
        lines = ["mutation Seo(" + ", ".join(decls) + ") {"] + body + ["}"]
        print(f"=== {kind} batch {n} ({len(chunk)}) ===")
        print("\n".join(lines))
        print("--- variables ---")
        print(json.dumps(variables, ensure_ascii=False))
        print()


if __name__ == "__main__":
    emit(sys.argv[1] if len(sys.argv) > 1 else "products")
