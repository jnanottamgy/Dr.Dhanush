"""SEO titles and meta descriptions for every product, collection and page.

Source of truth, like `catalogue/descriptions.py`. The store is pushed from
here, never edited in the Shopify admin, so a change survives and is reviewable.

RULES THAT MADE THESE, and that any edit must keep:

1. The theme appends " – Malnad Products" to the title tag unless the SEO title
   already contains the shop name (`snippets/meta-tags.liquid`). So SEO titles
   carry NO shop name and stay at or under TITLE_MAX, and the rendered tag lands
   inside Google's ~60-character display.
2. Every title leads with the words a customer actually types, and carries the
   pack size. "Black Pepper" is a dictionary entry; "Malnad Black Pepper 100 g"
   is a purchase.
3. Local names are kept where they ARE the search term — nellikai, sikakai,
   antuvala, sasive, chekke, marati moggu, kishmish, elakki. A Kannada-speaking
   customer does not search "Indian gooseberry powder".
4. NO HEALTH CLAIMS, anywhere. Same rule as the product descriptions: nothing
   about immunity, diabetes, cholesterol, antioxidants or any named condition.
   The three home-care lines say "Not a food." in their meta description too.
5. NO PRICES in meta descriptions. They change; a stale snippet in Google that
   undercuts the live price is a consumer-law problem, not just an annoyance.
6. Each description is unique. Duplicated meta descriptions across 57 pages is
   the single most common way a small catalogue gets flattened in search.
7. Origin is the differentiator and it appears wherever it is true — Horanadu,
   Kalasa, Koppa, Chikkamagaluru, Malnad, Western Ghats. Nobody else ranks for
   "marati moggu online"; everybody competes for "buy almonds".

Push with the GraphQL emitted by `emit_product_mutations()`.
"""

TITLE_MAX = 42        # + " – Malnad Products" (18) = 60
DESC_MIN, DESC_MAX = 110, 160

# handle -> (seo_title, seo_description)
PRODUCTS = {
    # ---- Whole spices (17) -------------------------------------------------
    "black-pepper": (
        "Malnad Black Pepper 100 g — Whole",
        "Whole black peppercorns grown on the shade trees of the Malnad coffee "
        "estates, weighed and packed to order at Horanadu. 100 g pack."),
    "cloves-lavanga": (
        "Whole Cloves (Lavanga) 100 g",
        "Dark, oily whole cloves that still bend rather than snap. Packed to "
        "order at Horanadu, Chikkamagaluru. 100 g pack, delivered across India."),
    "green-cardamom": (
        "Green Cardamom (Elakki) 100 g",
        "Whole green cardamom pods dried with the seeds still soft inside. For "
        "chai, payasa and sweets. Packed to order at Horanadu. 100 g pack."),
    "black-cardamom": (
        "Black Cardamom 100 g — Whole Pods",
        "Large smoke-dried black cardamom pods, deep and resinous — one pod "
        "carries a whole pot of biryani or dal. Packed to order. 100 g pack."),
    "nutmeg": (
        "Whole Nutmeg 100 g — Jaikai",
        "Whole nutmeg to grate fresh, because ground nutmeg loses its warmth "
        "faster than almost any spice. Packed to order at Horanadu. 100 g pack."),
    "jathipathri-mace": (
        "Jathipathri (Mace) 100 g",
        "The lacy red aril that wraps the nutmeg, dried to brittle amber blades. "
        "Finer and more floral than nutmeg. Packed to order. 100 g pack."),
    "chekke-cinnamon-bark": (
        "Chekke — Cinnamon Bark 100 g",
        "Cinnamon bark in rough quills, as it comes off the tree. Snap a piece "
        "into rice or a decoction. Packed to order at Horanadu. 100 g pack."),
    "star-anise": (
        "Whole Star Anise 100 g",
        "Whole star anise dried to eight-pointed wooden flowers — sweet, "
        "liquorice-like, and quiet in a large pot. Packed to order. 100 g pack."),
    "fennel-seed": (
        "Fennel Seed (Sompu) 100 g",
        "Pale green fennel seed, sweet and cooling. Chewed after a meal, "
        "tempered into a curry, or ground into masala. 100 g, packed to order."),
    "shahi-jeera": (
        "Shahi Jeera 100 g — Black Caraway",
        "Black caraway: slimmer, darker and more perfumed than ordinary cumin. "
        "Used where a dish wants depth without earthiness. 100 g pack."),
    "kasturi-menthi": (
        "Kasturi Menthi 100 g — Methi Leaves",
        "Dried fenugreek leaves, crushed between the palms at the end of "
        "cooking. Faintly bitter and hard to substitute. 100 g, packed to order."),
    "marati-moggu": (
        "Marati Moggu 100 g — Kapok Buds",
        "Kapok buds, the Karnataka spice that sits in bisi bele bath and local "
        "masala blends. Somewhere between clove and pepper. 100 g pack."),
    "naga-kesari-moggu": (
        "Naga Kesari Moggu 100 g",
        "A dried flower bud used in Malnad and Karnataka masala blends — one of "
        "those spices that rarely leaves the region. 100 g, packed to order."),
    "kalhoo": (
        "Kalhoo 100 g — Malnad Spice",
        "A Malnad spice used in the local masala blends around Horanadu. It "
        "rarely travels beyond these hills. 100 g pack, delivered across India."),
    "mintiya": (
        "Mintiya 100 g — Malnad Spice",
        "A Malnad spice from the kitchens around Horanadu, used in the masalas "
        "of this region. Not found in a city grocery. 100 g, packed to order."),
    "palavele": (
        "Palavele 100 g — Malnad Spice",
        "A Malnad spice, part of the blending tradition around Horanadu and "
        "Kalasa. Uncommon outside the district. 100 g pack, packed to order."),
    "sasive-mustard-seed": (
        "Sasive — Mustard Seed 100 g",
        "Small dark mustard seed for the tempering pan. Wait for the crackle "
        "before anything else goes in. 100 g, weighed and packed to order."),

    # ---- Masala and powders (7) -------------------------------------------
    "swad-horanadu-bisibele-bath-powder": (
        "Bisibele Bath Powder 250 g — Swad",
        "Swad Horanadu's blend for bisi bele bath, ground in small batches at "
        "Horanadu. Stir through rice, dal and vegetables, finish with ghee."),
    "swad-horanadu-garam-masala-powder": (
        "Swad Garam Masala Powder 250 g",
        "A warm, dark garam masala ground in small batches at Horanadu. Added "
        "late in cooking, where its aroma survives rather than boils away."),
    "swad-horanadu-palav-powder": (
        "Swad Palav (Pulao) Powder 250 g",
        "Our pulao masala from Horanadu. Bloom it in ghee with the rice before "
        "the water goes in and it will carry the whole pot. 250 g pack."),
    "swad-horanadu-puliyogare-powder": (
        "Swad Puliyogare Powder 250 g",
        "The tamarind-rice masala ground the Horanadu way. Stir into cooked "
        "rice with sesame oil and let it sit — puliyogare is better an hour on."),
    "swad-horanadu-rasam-powder": (
        "Swad Rasam Powder 250 g",
        "Pepper-forward rasam powder from Horanadu, made for the thin, sharp "
        "rasam that ends a Malnad meal rather than the thick kind. 250 g."),
    "swad-horanadu-sambar-powder": (
        "Swad Sambar Powder 250 g",
        "Sambar powder ground at Horanadu and balanced for the vegetables of "
        "this region. A steady everyday masala rather than a fiery one."),
    "horanadu-nellikai-powder": (
        "Nellikai (Amla) Powder 200 g",
        "Dried Indian gooseberry ground fine, from Annapoorneshwari Spices at "
        "Horanadu. Sharp and sour, used in the kitchen and in hair care."),

    # ---- Coffee (3) --------------------------------------------------------
    "swad-instant-coffee": (
        "Swad Instant Coffee — Malnad",
        "Instant coffee powder from our own Horanadu kitchen. Spoon it into hot "
        "milk or water for a quick cup with the body of a Malnad brew."),
    "swad-malnad-premium-coffee-powder-filter": (
        "Swad Filter Coffee Powder — Malnad",
        "Coffee powder ground for the traditional South Indian filter. Pack the "
        "dabara, let the decoction drip, top with hot milk. 250 g and 500 g."),
    "swad-malnad-premium-coffee-powder-nice": (
        "Swad Nice Coffee Powder — Malnad",
        "Our everyday grind from Horanadu, smoother and lighter than the filter "
        "blend. Good at any hour and forgiving if you like it milky."),

    # ---- Tea (3) -----------------------------------------------------------
    "malnad-chai-premium-malnad-tea-powder": (
        "Malnad Chai Tea Powder — 250 g to 1 kg",
        "Our own tea powder, blended and packed at Horanadu. Brisk and "
        "full-bodied, made for chai boiled hard with milk, ginger and cardamom."),
    "sanjivni-special-tea": (
        "Sanjivni Special Tea 1 kg — Kalasa",
        "Tea powder from Nagashree Coffee Works at Kalasa, a neighbour of ours "
        "in the Malnad hills. A strong granular leaf that takes milk well."),
    "qtf-tea-guard-hitlow-tea-factory": (
        "QTF Tea 1 kg — Koppa Estate Tea",
        "Tea from the Guard-Hitlow Tea Factory at Koppa, sold by the kilo. A "
        "workaday estate tea for a household that gets through a lot of chai."),

    # ---- Oils (3) ----------------------------------------------------------
    "ghani-pressed-copra-coconut-oil": (
        "Ghani-Pressed Coconut Oil 1 Litre",
        "Coconut oil from Shree Durga Industries, crushed in the traditional "
        "wooden ghani rather than heat-extracted, so it keeps its coconut smell."),
    "aaradhya-pure-double-filtered-coconut-oil": (
        "Aaradhya Coconut Oil — 500 ml / 1 L",
        "Double-filtered coconut oil, clear and clean-smelling. For cooking, for "
        "the tempering pan, and for hair, the way it has always been used here."),
    "kalpatharu-special-double-filtered-pure-coconut-oil": (
        "Kalpatharu Coconut Oil 1.72 kg Tin",
        "Coconut oil from Ganesh Flour and Oil Mill, double filtered and sold in "
        "the large tin — the size a family that cooks in coconut oil gets through."),

    # ---- Syrups and squashes (9) ------------------------------------------
    "nisarga-amla-health-drink": (
        "Nisarga Amla Drink 700 ml",
        "An amla concentrate from Malnad's Nisarga. Bracingly sour on its own, "
        "so dilute it well with cold water. 700 ml bottle from the Malnad hills."),
    "malnad-s-nisarga-banana-stem-squash": (
        "Banana Stem Squash 500 ml — Nisarga",
        "A squash pressed from banana stem, a Malnad kitchen staple rarely seen "
        "in a bottle. Light, grassy and clean-tasting. Dilute to serve."),
    "malnad-s-nisarga-jamun-squash": (
        "Jamun Squash 700 ml — Malnad Nisarga",
        "Jamun squash from Malnad's Nisarga — deep purple, tart and astringent "
        "in the way only jamun is. Mix with cold water and ice. 700 ml."),
    "nanjangud-suruchi-s-ginger-lime-syrup": (
        "Ginger Lime Syrup 700 ml — Suruchi's",
        "Ginger and lime cordial from Nanjangud Suruchi's. Sharp and warming, "
        "good with soda as much as with plain water. 700 ml bottle."),
    "nanjangud-suruchi-s-grapes-syrup": (
        "Grapes Syrup 700 ml — Suruchi's",
        "Grape syrup from Nanjangud Suruchi's. Sweet and simple, the one "
        "children ask for. Dilute to taste. 700 ml bottle, delivered in India."),
    "nanjangud-suruchi-s-jamboo-syrup": (
        "Jamboo Syrup 700 ml — Suruchi's",
        "Jamboo syrup from Nanjangud Suruchi's, dark and fruity. Mix with "
        "chilled water for a summer drink. 700 ml bottle from Nanjangud."),
    "nanjangud-suruchi-s-sugarless-jamboo-syrup": (
        "Sugarless Jamboo Syrup 700 ml",
        "The same Nanjangud Suruchi's jamboo syrup, made without added sugar, "
        "for a household that would rather sweeten its own glass. 700 ml."),
    "hallimane-kokam-syrup": (
        "Hallimane Kokam Syrup 700 ml",
        "Kokam syrup from Hallimane — sour, rose-red and cooling, the coastal "
        "answer to a hot afternoon. Dilute with cold water and salt lightly."),
    "nanjangud-suruchi-s-diabeat": (
        "Diabeat 700 ml — Nanjangud Suruchi's",
        "A herbal decoction from Nanjangud Suruchi's, Nanjangud, supplied "
        "exactly as bottled by the maker. 700 ml bottle."),

    # ---- Seeds (6) ---------------------------------------------------------
    "chia-seeds": (
        "Chia Seeds 150 g",
        "Tiny grey-black seeds that swell into a soft gel in water. Stir into "
        "drinks or curd, or soak overnight with milk and fruit. 150 g pack."),
    "sabja-seeds": (
        "Sabja (Basil) Seeds 150 g",
        "The classic falooda and nimbu pani seed. Soak a few minutes and it "
        "blooms into a translucent jelly around a dark centre. 150 g pack."),
    "flax-seeds": (
        "Flax Seeds 150 g — Whole",
        "Glossy brown flax sold whole so it keeps. Dry-roast and coarsely grind "
        "at home, or use it the Karnataka way as a chutney powder. 150 g."),
    "magaz-seeds": (
        "Magaz Seeds 150 g — Melon Kernels",
        "Pale flat melon seed kernels, ground into rich gravies and korma bases "
        "or scattered over sweets. 150 g pack, delivered across India."),
    "pumpkin-seeds": (
        "Pumpkin Seeds 150 g",
        "Green pumpkin kernels, good raw or lightly toasted with salt. Keeps "
        "well in an airtight jar once opened. 150 g pack."),
    "sunflower-seeds": (
        "Sunflower Seeds 150 g",
        "Hulled sunflower kernels that turn nutty after a few minutes in the "
        "pan. Good on salads, in chutney powder, or from the jar. 150 g pack."),

    # ---- Dry fruits and nuts (6) ------------------------------------------
    "badam-almonds": (
        "Badam (Almonds) 500 g",
        "Whole almonds weighed out and packed when you order. Soak overnight "
        "and slip the skins off, or grind them into badam milk and halwa."),
    "pista-pistachios": (
        "Pista (Pistachios) 500 g",
        "Pistachios in the shell, marked export quality on the pack. Salted, "
        "green inside, and hard to stop eating. 500 g pack."),
    "hayat-organic-raisins-dry-grapes": (
        "Hayat Raisins 500 g — Kishmish",
        "Kishmish from Pahul Agro. Plump golden raisins for payasa, pulao and "
        "sweets, or for eating by the handful. 500 g pack."),
    "dates": (
        "Dates (Khajur) 500 g",
        "Soft everyday dates, weighed and packed to order at Horanadu. Good in "
        "the lunchbox, in sweets, or blended into a milkshake. 500 g pack."),
    "special-dates": (
        "Special Dates 500 g — Premium Grade",
        "Our larger, softer grade of date — fleshier and darker, with more "
        "caramel to it. The ones we keep for guests. 500 g, packed to order."),
    "mixed-dry-fruits-gift-pack": (
        "Mixed Dry Fruits Gift Pack 150 g",
        "A mixed pack of dry fruits and nuts from Karthik Traders, ready to "
        "hand over at a festival or a house visit. 150 g gift pack."),

    # ---- Home and personal care (3) — NOT FOOD -----------------------------
    "antuvala-soapnut-powder": (
        "Antuvala (Soapnut) Powder 200 g",
        "Soapnut ground to a powder by Annapoorneshwari at Kalasa. Mixed with "
        "warm water it lathers gently — the traditional hair wash. Not a food."),
    "sikakai-shikakai-powder": (
        "Sikakai (Shikakai) Powder 200 g",
        "Shikakai powder from Annapoorneshwari at Kalasa, mixed into a paste "
        "for washing hair, often together with soapnut. Not a food. 200 g."),
    "soapnut-whole": (
        "Soapnut (Antuvala) Whole 150 g",
        "Whole soapnuts as they come off the tree. Soak a few and squeeze for a "
        "mild natural lather — hair, delicate washing, laundry. Not a food."),
}

# handle -> (seo_title, seo_description)
COLLECTIONS = {
    "whole-spices": (
        "Whole Spices from the Malnad Hills",
        "Pepper, cardamom, cloves and cinnamon bark alongside the Malnad spices "
        "that rarely travel — marati moggu, naga kesari, kalhoo and palavele."),
    "masala-powders": (
        "Swad Horanadu Masala Powders",
        "Puliyogare, rasam, sambar, palav, bisi bele bath and garam masala, "
        "ground in small batches at Horanadu for everyday Malnad cooking."),
    "coffee": (
        "Malnad Coffee Powder — Swad Horanadu",
        "Filter, nice and instant coffee powder from Horanadu in the "
        "Chikkamagaluru coffee country. Ground in small batches, packed to order."),
    "tea": (
        "Malnad Tea Powder — Chai by the Kilo",
        "Our own Malnad Chai alongside estate tea from Kalasa and Koppa. Strong, "
        "granular leaf made for chai boiled hard with milk and ginger."),
    "oils": (
        "Coconut Oil — Ghani-Pressed & Filtered",
        "Ghani-pressed and double-filtered coconut oil from Malnad mills, in "
        "bottles and the large family tin. For cooking and for hair."),
    "syrups-squashes": (
        "Syrups & Squashes from the Malnad",
        "Kokam, jamun, amla, banana stem and ginger-lime, bottled by small "
        "makers across the Malnad and Nanjangud. Dilute and serve cold."),
    "seeds": (
        "Chia, Sabja, Flax & Melon Seeds",
        "Chia, sabja, flax, magaz, pumpkin and sunflower seed, weighed and "
        "packed to order at Horanadu. Delivered anywhere in India."),
    "dry-fruits-nuts": (
        "Dry Fruits & Nuts — Badam, Pista, Dates",
        "Almonds, pistachios, dates, raisins and mixed gift packs, weighed and "
        "packed the day you order rather than sitting on a shelf."),
    "home-personal-care": (
        "Soapnut & Shikakai — Traditional Hair Care",
        "Antuvala and sikakai powder and whole soapnuts from Kalasa, the "
        "traditional Malnad wash for hair and for delicate laundry. Not foods."),
}

# handle -> (seo_title, seo_description). Pages store SEO as `global` metafields.
PAGES = {
    "about": (
        "About Malnad Products — Horanadu",
        "Malnad Variety Centre has traded at Horanadu, Chikkamagaluru since "
        "1999. Spices, coffee, tea and estate goods, weighed and packed to order."),
    "contact": (
        "Contact Us — Malnad Products, Horanadu",
        "Reach Malnad Products at Devaramane, Horanadu Post, Kalasa Taluk, "
        "Chikkamagaluru 577181. Phone, email and a message form. FSSAI licensed."),
}

# The homepage title and meta description are NOT settable through the Admin
# API. They live in Shopify admin → Online Store → Preferences, and someone with
# a browser has to paste them in. Kept here so the wording is version-controlled
# and matches the rest.
HOMEPAGE_TITLE = "Malnad Products — Spices, Coffee & Estate Goods from Horanadu"
HOMEPAGE_DESCRIPTION = (
    "Buy Malnad spices, coffee, tea and estate goods direct from Horanadu, "
    "Chikkamagaluru. Weighed and packed the day you order. Delivered across "
    "India. Trading since 1999.")


def check():
    """Fail loudly rather than push something that renders badly."""
    problems = []
    seen_titles, seen_descs = {}, {}
    banned = ("immunity", "cholesterol", "antioxidant", "diabet", "cure",
              "treats", "disease", "weight loss", "detox")
    for group, data in (("product", PRODUCTS), ("collection", COLLECTIONS),
                        ("page", PAGES)):
        for handle, (title, desc) in data.items():
            where = f"{group}:{handle}"
            if len(title) > TITLE_MAX:
                problems.append(f"{where} title {len(title)} > {TITLE_MAX}: {title}")
            if not DESC_MIN <= len(desc) <= DESC_MAX:
                problems.append(f"{where} description {len(desc)} chars: {desc}")
            low = (title + " " + desc).lower()
            for word in banned:
                # "Diabeat" is the maker's own product name, not a claim we make.
                if word == "diabet" and "diabeat" in low:
                    continue
                if word in low:
                    problems.append(f"{where} contains banned word '{word}'")
            if title in seen_titles:
                problems.append(f"{where} duplicate title with {seen_titles[title]}")
            if desc in seen_descs:
                problems.append(f"{where} duplicate description with {seen_descs[desc]}")
            seen_titles[title], seen_descs[desc] = where, where
    return problems


if __name__ == "__main__":
    import sys
    issues = check()
    for issue in issues:
        print("FAIL", issue)
    print(f"{len(PRODUCTS)} products, {len(COLLECTIONS)} collections, "
          f"{len(PAGES)} pages — {len(issues)} problems")
    sys.exit(1 if issues else 0)
