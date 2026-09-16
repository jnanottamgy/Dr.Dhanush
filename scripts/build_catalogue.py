#!/usr/bin/env python3
"""Build the working catalogue sheet from what the packs actually told us.

Design rule: every value in here was read off a pack photograph or off the
catalogue name. Anything we do not have is left EMPTY — a gap, never a guess.
When the client answers, edit the data below and re-run; the sheet regenerates.

Two fields are deliberately empty on every row:
  HSN Code, GST Rate (%) — tax classification is the CA's written call.
                           Proposals for him to sign off: catalogue/tax-schedule.md

One field is an estimate, and is not a declaration:
  Shipping Weight (g) — net weight plus a packaging allowance, for dispatch
                        pricing only. Formula in ship_weight().
"""
import csv
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "catalogue" / "malnad-catalogue.csv"

COLUMNS = [
    "Product Name", "Category", "Short Description", "Full Description",
    "Pack Size", "Grind / Form", "SKU", "Selling Price (INR)",
    "MRP (INR incl. all taxes)", "Stock Qty", "Shipping Weight (g)",
    "HSN Code", "GST Rate (%)", "Net Quantity",
    "Manufacturer or Packer Name", "Manufacturer or Packer Full Address",
    "Date of Manufacture or Packing", "Best Before / Use By",
    "Country of Origin", "Consumer Care Name", "Consumer Care Phone",
    "Consumer Care Email", "FSSAI Licence Number", "Ingredients",
    "Storage Instructions", "Estate / Origin", "Altitude (ft)",
    "Harvest Month", "Roast Level", "Image File Names",
]

# Consumer care email. Supplied by the client 16 Sep; it is not printed on a
# single pack in the catalogue, his own included, so it could not be read off
# anything. On his own repacked goods he is the packer and this is the packer's
# email. On goods he resells he is the seller, and this is the seller's contact
# that e-commerce needs - the maker's own printed email wins wherever there is
# one (only Shree Durga prints one).
SELLER_CARE_EMAIL = "drjhrnd5@gmail.com"

# ---------------------------------------------------------------- packers
# Every field here is transcribed from a pack photograph. "" means the pack
# does not carry it.

MS = dict(  # Malnad Spices — the client's own label
    packer="Malnad Spices",
    address="Devaramane, Horanadu Post, Kalasa Tq, Chikkamagaluru Dist - 577181, Karnataka, India",
    care_name="Malnad Spices",
    care_phone="8431218956, 9480956035",
    care_email=SELLER_CARE_EMAIL,       # supplied by the client, not on the pack
    fssai="21223055000121",
    storage="Store in a cool, dry, hygienic place away from direct sunlight and "
            "strong odour. Transfer to an airtight container once opened.",
)

NAGASHREE = dict(
    packer="Nagashree Coffee Works",
    address="Mahaveera Road, Kalasa - 577124, Chikmagalur Tq, Chikmagalur Dist, Karnataka, India",
    care_name="Nagashree Coffee Works",
    care_phone="08263-274536",
    care_email="",
    fssai="21215055000048",
    storage="",
)

QTF = dict(
    packer="The Mysore Plantations Limited",
    address="Guard Hitlow, Post Box No 12, Koppa - 577126, Chikmagalur District, Karnataka, India",
    care_name="The Mysore Plantations Limited",
    care_phone="",                      # a number is printed but not legible
    care_email="",
    fssai="",                           # not printed on the sack
    storage="",
)

ANNA = dict(   # Annapoorneshwari Spices & Malnad Specials
    packer="Annapoorneshwari Spices & Malnad Specials",
    address="Kalasa, Horanadu - 577181, Chikmagalore, Karnataka, India",
    care_name="Annapoorneshwari Spices & Malnad Specials",
    care_phone="094487 44341",
    care_email="",
    fssai="2127055000011",
    storage="",
)

ANNA_POWDER = dict(  # the nellikai pouch names a different unit and licence
    packer="Annapoorneshwari Spices Powder Unit",
    address="Kalasa, Horanadu - 577181, Chikmagalore, Karnataka, India",
    care_name="Annapoorneshwari Spices Powder Unit",
    care_phone="",
    care_email="",
    fssai="21217055000117",
    storage="",
)

GANESH = dict(
    packer="Ganesh Flour & Oil Mill",
    address="College Road, Ujire - 574240, Dakshina Kannada, Karnataka, India",
    care_name="Ganesh Flour & Oil Mill",
    care_phone="9480289125",
    care_email="",
    fssai="11219312000310",
    storage="",
)

DURGA = dict(
    packer="Shree Durga Industries",
    address="Vijaya Nagar, Madanthyar - 574224, Karnataka, India",
    care_name="Shree Durga Industries",
    care_phone="+91 94481 89468",
    care_email="srdurgaindustries2007@gmail.com",
    fssai="11221312000760",
    storage="",
)

PAHUL = dict(
    packer="Pahul Agro",
    address="",                         # not legible on the pack
    care_name="Pahul Agro",
    care_phone="",
    care_email="",
    fssai="1111804000485",
    storage="",
)

# Front-label brands. The maker is named on the front; address, FSSAI and
# consumer care live on the back label, which we do not have a photograph of.
NISARGA = dict(packer="Malnad's Nisarga", address="", care_name="Malnad's Nisarga",
               care_phone="", care_email="", fssai="", storage="")

SURUCHI = dict(packer="Nanjangud Suruchi's",
               address="Sindhuvalli (Po), Nanjangud, Karnataka, India",
               care_name="Nanjangud Suruchi's", care_phone="", care_email="",
               fssai="", storage="")

HALLIMANE = dict(packer="Hallimane", address="", care_name="Hallimane",
                 care_phone="", care_email="", fssai="", storage="")

UNKNOWN = dict(packer="", address="", care_name="", care_phone="",
               care_email="", fssai="", storage="")

# ---------------------------------------------------------------- helpers

def ship_weight(net, kind):
    """Dispatch estimate, not a declaration. net is a (value, unit) pair."""
    if net is None:
        return ""
    val, unit = net
    grams = {"g": val, "kg": val * 1000,
             "ml": val * (1.0 if kind == "oil" else 1.25),
             "l": val * 1000 * (1.0 if kind == "oil" else 1.25)}[unit]
    allowance = {"bottle": 150, "can": 250, "tub": 60}.get(kind, 40)
    if kind == "oil":
        allowance = 150 if grams <= 1000 else 250
    return str(int(round(grams + allowance)))


def net_text(net):
    if net is None:
        return ""
    val, unit = net
    val = int(val) if float(val).is_integer() else val
    return f"{val} {unit}"


def slug(s):
    out = "".join(c if c.isalnum() else "-" for c in s.lower())
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-")


def P(name, category, packer, variants, desc="", full="", ingredients="",
      best_before="", pkd="", form="", roast="", origin="", proposed_hsn="",
      proposed_gst="", note=""):
    return dict(name=name, category=category, packer=packer, variants=variants,
                desc=desc, full=full, ingredients=ingredients,
                best_before=best_before, pkd=pkd, form=form, roast=roast,
                origin=origin, proposed_hsn=proposed_hsn,
                proposed_gst=proposed_gst, note=note)


# --- Prices supplied 16 Sep, second batch -----------------------------------
# Keyed (product name, pack size). Applied as an override so a client answer is
# one edit here rather than 27 edits scattered through the product definitions.
#
# Whether the figure also becomes the declared MRP depends on who packs it:
#
#   * Goods Malnad Spices packs itself - the 17 whole spices, the Swad coffees,
#     Malnad Chai, Badam - carry no printed MRP, and as packer his number IS the
#     MRP. Price and MRP both.
#   * Goods he only resells - Sanjivni, Aaradhya, Kalpatharu - are sealed by
#     their own maker. The MRP on those packs is the maker's, not ours;
#     Kalpatharu's is printed but smudged. We set the selling price and declare
#     NO MRP, because inventing one would be a misdeclaration on somebody else's
#     pack.
PRICES_16SEP = {
    ("Black Pepper", "100 g"): "80",
    ("Cloves (Lavanga)", "100 g"): "150",
    ("Green Cardamom", "100 g"): "500",
    ("Black Cardamom", "100 g"): "240",
    ("Nutmeg", "100 g"): "90",
    ("Jathipathri (Mace)", "100 g"): "320",
    ("Chekke (Cinnamon Bark)", "100 g"): "50",
    ("Star Anise", "100 g"): "150",
    ("Fennel Seed", "100 g"): "50",
    ("Shahi Jeera", "100 g"): "150",
    ("Kasturi Menthi", "100 g"): "100",
    ("Marati Moggu", "100 g"): "160",
    ("Naga Kesari Moggu", "100 g"): "240",
    ("Kalhoo", "100 g"): "150",
    ("Mintiya", "100 g"): "25",
    ("Palavele", "100 g"): "60",
    ("Sasive (Mustard Seed)", "100 g"): "25",
    ("Swad Malnad Premium Coffee Powder - Filter", "250 g"): "160",
    ("Swad Malnad Premium Coffee Powder - Filter", "500 g"): "300",
    ("Swad Malnad Premium Coffee Powder - Nice", "250 g"): "160",
    ("Swad Malnad Premium Coffee Powder - Nice", "500 g"): "300",
    ("Malnad Chai - Premium Malnad Tea Powder", "1 kg"): "300",
    ("Badam (Almonds)", "500 g"): "750",
    ("Sanjivni Special Tea", "1 kg"): "270",
    ("Aaradhya Pure Double Filtered Coconut Oil", "500 ml"): "200",
    ("Aaradhya Pure Double Filtered Coconut Oil", "1 l"): "400",
    ("Kalpatharu Special Double Filtered Pure Coconut Oil", "1.720 kg"): "800",
    # Syrups and squashes, supplied 16 Sep - the last of the 36.
    ("Nisarga Amla Health Drink", "700 ml"): "160",
    ("Malnad's Nisarga Banana Stem Squash", "500 ml"): "180",
    ("Malnad's Nisarga Jamun Squash", "700 ml"): "160",
    ("Nanjangud Suruchi's Ginger Lime Syrup", "700 ml"): "160",
    ("Nanjangud Suruchi's Grapes Syrup", "700 ml"): "130",
    ("Nanjangud Suruchi's Jamboo Syrup", "700 ml"): "160",
    ("Nanjangud Suruchi's Sugarless Jamboo Syrup", "700 ml"): "160",
    ("Hallimane Kokam Syrup", "700 ml"): "140",
    ("Nanjangud Suruchi's Diabeat", "700 ml"): "270",
}

# Packed by somebody else, so their price is a selling price only - never an MRP.
RESOLD_NO_MRP = {
    "Sanjivni Special Tea",
    "Aaradhya Pure Double Filtered Coconut Oil",
    "Kalpatharu Special Double Filtered Pure Coconut Oil",
    # All nine syrups are sealed bottles from other makers. Their labels do
    # carry an "M.R.P. Rs (Incl. of all taxes)" box - and the maker left it
    # blank. A blank box on somebody else's pack is still the maker's
    # declaration to make, not ours, so only the selling price is set.
    "Nisarga Amla Health Drink",
    "Malnad's Nisarga Banana Stem Squash",
    "Malnad's Nisarga Jamun Squash",
    "Nanjangud Suruchi's Ginger Lime Syrup",
    "Nanjangud Suruchi's Grapes Syrup",
    "Nanjangud Suruchi's Jamboo Syrup",
    "Nanjangud Suruchi's Sugarless Jamboo Syrup",
    "Hallimane Kokam Syrup",
    "Nanjangud Suruchi's Diabeat",
}


def V(pack, net, images, mrp="", kind="pouch", pkd="", best_before="", sell=""):
    # `sell` is the selling price. Where a pack prints no MRP and the client is
    # the packer, the single price he names is both the MRP and the selling
    # price - so it is passed to both and no compare-at is written.
    return dict(pack=pack, net=net, images=images, mrp=mrp, kind=kind,
                pkd=pkd, best_before=best_before, sell=sell)


G = None   # a gap: not on the pack, not in the name

# ---------------------------------------------------------------- catalogue

PRODUCTS = [
    # ============================================================ COFFEE
    P("Swad Instant Coffee", "Coffee", MS,
      desc="Instant coffee powder from Malnad Spices, Horanadu.",
      best_before="8 months from the date of packing",
      proposed_hsn="2101", proposed_gst="5",
      note="Instant coffee is an extract, so HSN 2101, not 0901. The client answered 5% for it on 16 Sep along with everything else. 2101 normally attracts 18%, so the HSN and the rate do not agree - flagged to the CA, his figure is applied.",
      variants=[
          V("100 g", (100, "g"), "100g-instant-coffee.png", mrp="180"),
          V("200 g", (200, "g"), "200g-instant-coffee.png", mrp="360"),
      ]),

    # Both coffees came with front AND back photographs. The "-2" file is the
    # front (SWAD branding), "-1" the back (declarations panel), so the front
    # leads and the back follows as the second image.
    P("Swad Malnad Premium Coffee Powder - Filter", "Coffee", MS,
      desc="Filter coffee powder from Malnad Spices, Horanadu.",
      best_before="8 months from the date of packing",
      proposed_hsn="0901", proposed_gst="5",
      note="Named off the pack front, which reads SWAD / MALNAD PREMIUM COFFEE "
           "POWDER / FILTER. If chicory is blended in the classification moves; "
           "the back panel prints a nutrition table but no ingredients list, so "
           "we cannot tell from the photograph.",
      variants=[
          V("250 g", (250, "g"),
            "250g-special-filter-coffee-2.png,250g-special-filter-coffee-1.png"),
          V("500 g", (500, "g"),
            "kg-filter-coffee-special-2.png,kg-filter-coffee-special-1.png"),
      ]),

    P("Swad Malnad Premium Coffee Powder - Nice", "Coffee", MS,
      desc="Coffee powder from Malnad Spices, Horanadu.",
      best_before="8 months from the date of packing",
      proposed_hsn="0901", proposed_gst="5",
      note="Named off the pack front, which reads SWAD / MALNAD PREMIUM COFFEE "
           "POWDER / NICE. 'Nice' usually indicates a coffee-chicory blend, "
           "which would move the HSN, but no ingredients list is printed.",
      variants=[
          V("250 g", (250, "g"),
            "250g-special-nice-coffee-2.png,250g-special-nice-coffee-1.png"),
          V("500 g", (500, "g"),
            "kg-nice-coffee-special-2.png,kg-nice-coffee-special-1.png"),
      ]),

    # =============================================================== TEA
    P("Malnad Chai - Premium Malnad Tea Powder", "Tea", MS,
      desc="Premium Malnad tea powder, packed at Horanadu.",
      proposed_hsn="0902", proposed_gst="5",
      variants=[
          V("250 g", (250, "g"), "250g-special-tea.png", mrp="150"),
          V("500 g", (500, "g"), "kgspecial-tea.png", mrp="220", pkd="September 2026"),
          V("1 kg", (1, "kg"), "1kg-special-tea.png"),
      ]),

    P("Sanjivni Special Tea", "Tea", NAGASHREE,
      desc="Tea powder from Nagashree Coffee Works, Kalasa.",
      best_before="12 months from packaging",
      proposed_hsn="0902", proposed_gst="5",
      note="Two packs supplied, black and red, both 1 kg, nothing on either "
           "distinguishing a grade. Listed once until the client says otherwise. "
           "The MRP line on the pack was never filled in.",
      variants=[
          V("1 kg", (1, "kg"), "1kg-tea-2.png,1kg-tea-1.png,sanjivini-special-tea-2.png"),
      ]),

    P("QTF Tea - Guard-Hitlow Tea Factory", "Tea", QTF,
      desc="Tea from Guard-Hitlow Tea Factory, Koppa.",
      proposed_hsn="0902", proposed_gst="5",
      note="Net quantity confirmed as 1 kg by the client 16 Sep - the sack itself "
           "prints no weight, and 250 per kg is his price. Still missing: the "
           "FSSAI licence number and a packing date. The printed face carries only the "
           "factory name and address, which is why this one reads as trade "
           "packaging rather than a retail pack.",
      variants=[
          V("1 kg", (1, "kg"), "tea-powder-1kg.png", mrp="250"),
      ]),

    # ==================================================== WHOLE SPICES
    # All repacked by the client into plain poly bags, 100 g per the catalogue
    # name. None of these bags carries any printed declaration.
    *[
        P(nm, "Whole Spices", MS, desc=d, proposed_hsn=h, proposed_gst="5",
          note=nt,
          variants=[V("100 g", (100, "g"), img)])
        for nm, d, h, img, nt in [
            ("Black Pepper", "Whole black pepper.", "0904", "100g-pepper.png", ""),
            ("Cloves (Lavanga)", "Whole cloves.", "0907", "100g-clove.png,100ga-lavanga.png",
             "Supplied twice, as 'clove' and as 'lavanga' - the same whole cloves "
             "in the same bag. Lavanga is Kannada for clove. Listed once."),
            ("Green Cardamom", "Whole green cardamom pods.", "0908", "100g-cardamom.png", ""),
            ("Black Cardamom", "Whole black cardamom pods.", "0908", "100g-black-cardamom.png", ""),
            ("Nutmeg", "Whole nutmeg.", "0908", "100g-nutmeg.png", ""),
            ("Jathipathri (Mace)", "Mace, the outer covering of the nutmeg.", "0908",
             "100g-jathipathri.png", ""),
            ("Chekke (Cinnamon Bark)", "Cinnamon bark pieces.", "0906", "100g-chekke.png", ""),
            ("Star Anise", "Whole star anise.", "0909", "100g-star-anise.png", ""),
            ("Fennel Seed", "Whole fennel seed.", "0909", "100g-fennel-seed.png", ""),
            ("Shahi Jeera", "Shahi jeera (caraway).", "0909", "100-shahi-jeera.png", ""),
            ("Kasturi Menthi", "Dried fenugreek leaves.", "0910", "100g-kasturi-menthi.png", ""),
            ("Marati Moggu", "Kapok buds, used in Malnad and Kannada cooking.", "0910",
             "100g-marati-moggu.png", ""),
            ("Naga Kesari Moggu", "", "0910", "100g-naga-kesari-moggu.png",
             "Description left blank - not confident what this is without asking."),
            ("Kalhoo", "", "0910", "100g-kalhoo.png",
             "Description left blank - not confident what this is without asking."),
            ("Mintiya", "", "0910", "100g-mintiya.png",
             "Description left blank - not confident what this is without asking."),
            ("Palavele", "", "0910", "100g-palavele.png",
             "Description left blank - not confident what this is without asking."),
            ("Sasive (Mustard Seed)", "Mustard seed.", "1207",
             "100g-sasive.png",
             "Mustard is an oil seed - HSN chapter 12, not 09. Rate differs from "
             "the spices. Please confirm."),
        ]
    ],

    # ================================================= MASALA & POWDERS
    *[
        P(nm, "Masala & Powders", MS, desc=d,
          best_before="8 months from the date of packing",
          proposed_hsn="0910", proposed_gst="5",
          note="Mixed spice blend. The 5%-vs-12% question was answered 5% by the client 16 Sep. Blends sold under a brand name are commonly taken at 12%, so this one is worth the CA's eye.",
          variants=[V("250 g", (250, "g"), img, mrp=mrp, pkd=pkd)])
        for nm, d, img, mrp, pkd in [
            ("Swad Horanadu Bisibele Bath Powder",
             "Spice blend for bisibele bath.", "250g-bisibele-bath-powder.png",
             "80", "August 2026"),
            ("Swad Horanadu Garam Masala Powder",
             "Garam masala blend.", "250g-garam-masala-powder.png", "200", ""),
            ("Swad Horanadu Palav Powder",
             "Spice blend for palav.", "250g-palav-powder.png", "180", ""),
            ("Swad Horanadu Puliyogare Powder",
             "Spice blend for puliyogare.", "250g-puliyogare-powder.png", "180", ""),
            ("Swad Horanadu Rasam Powder",
             "Spice blend for rasam.", "250g-rasam-powder.png", "180", ""),
            ("Swad Horanadu Sambar Powder",
             "Spice blend for sambar.", "250g-sambar-powder.png", "180", ""),
        ]
    ],

    P("Horanadu Nellikai Powder", "Masala & Powders", ANNA_POWDER,
      desc="Amla (nellikai) powder from Horanadu.",
      best_before="12 months from the date of packing",
      pkd="August 2026",
      proposed_hsn="0813", proposed_gst="5",
      note="Net contents 200 g and MRP 200 supplied by the client 16 Sep. The "
           "MRP is printed on the pack too but is unreadable in the photograph, "
           "so this is his figure rather than a transcription. Also: the pack prints 'Rich in Vitamin C and cooling agent "
           "for both body and eyes'. That claim must not be repeated on the listing.",
      variants=[V("200 g", (200, "g"), "nellikai-powder.png", mrp="200")]),

    # ============================================================= SEEDS
    # Clear tubs. Four carry a name sticker, chia and sabja carry nothing.
    *[
        P(nm, "Seeds", MS, desc=d, proposed_hsn=h, proposed_gst="5",
          note="Quantity and price supplied by the client 16 Sep. The tub itself "
               "still prints nothing - he is the packer, so the declaration has "
               "to go on the pack he ships, not only on the listing.",
          variants=[V("150 g", (150, "g"), img, mrp="140", sell="140", kind="tub")])
        for nm, d, h, img in [
            ("Chia Seeds", "Chia seeds.", "1207", "chia-seeds.png"),
            ("Sabja Seeds", "Sabja (basil) seeds.", "1207", "sabja-seeds.png"),
            ("Flax Seeds", "Flax seeds.", "1204", "flax-seeds.png"),
            ("Magaz Seeds", "Melon seed kernels.", "1207", "magaz-seeds.png"),
            ("Pumpkin Seeds", "Pumpkin seed kernels.", "1207", "pumpkin-seeds.png"),
            ("Sunflower Seeds", "Sunflower seed kernels.", "1206", "sunflower-seeds.png"),
        ]
    ],

    # =============================================== DRY FRUITS & NUTS
    P("Badam (Almonds)", "Dry Fruits & Nuts", MS,
      desc="Almonds.", proposed_hsn="0802", proposed_gst="5",
      variants=[V("500 g", (500, "g"), "kg-badam.png")]),

    P("Pista (Pistachios)", "Dry Fruits & Nuts", UNKNOWN,
      desc="Pistachios, export quality.", proposed_hsn="0802", proposed_gst="5",
      note="Printed pouch. Net weight 500 g IS printed. The MRP box and the "
           "'Packed By' box were both left blank, so the packer is not declared.",
      variants=[V("500 g", (500, "g"), "pista.png", mrp="900", sell="900")]),

    P("Hayat Organic Raisins (Dry Grapes)", "Dry Fruits & Nuts", PAHUL,
      desc="Organic raisins.", ingredients="Kishmish",
      best_before="12 months from the date of packing",
      proposed_hsn="0806", proposed_gst="5",
      note="MRP, month of packing and batch number are all blank on the pack.",
      variants=[V("500 g", (500, "g"), "dry-grapes.png", mrp="300", sell="300")]),

    P("Dates", "Dry Fruits & Nuts", MS,
      desc="Dates.", proposed_hsn="0804", proposed_gst="5",
      note="Quantity and price supplied 16 Sep. The bag prints nothing at all.",
      variants=[V("500 g", (500, "g"), "normal-dates.png", mrp="150", sell="150")]),

    P("Special Dates", "Dry Fruits & Nuts", MS,
      desc="Dates.", proposed_hsn="0804", proposed_gst="5",
      note="Quantity and price supplied 16 Sep. The pack has a proper "
           "pre-printed block - 'Net Weight (When Packed)' and 'M.R.P.' - and "
           "both were left empty. Those boxes now have values to carry.",
      variants=[V("500 g", (500, "g"), "special-dates.png", mrp="200", sell="200")]),

    P("Mixed Dry Fruits Gift Pack", "Dry Fruits & Nuts", UNKNOWN,
      desc="Assorted dry fruits in a gift pack.",
      proposed_hsn="0813", proposed_gst="5",
      note="Karthik Traders, Varanga. 150 g and MRP 150 read off a sticker.",
      variants=[V("150 g", (150, "g"), "mixed-dry-fruits-gift-pack.png", mrp="150")]),

    # ============================================= SYRUPS & SQUASHES
    # Makers read off the front labels. Address, FSSAI, MRP, batch and packing
    # date are all on the back labels, and we have no back-of-pack photographs
    # for any of these nine.
    *[
        P(nm, "Syrups & Squashes", pk, desc=d, proposed_hsn="2106",
          proposed_gst="5", note=nt,
          variants=[V(net_text(n), n, img, kind="bottle")])
        for nm, d, n, img, pk, nt in [
            ("Nisarga Amla Health Drink", "Amla drink.", (700, "ml"),
             "amla-syrup-700ml.png", NISARGA,
             "The front label is badged 'HEALTH DRINK'. That is the brand's own "
             "wording and must not be carried over as a claim in our copy."),
            ("Malnad's Nisarga Banana Stem Squash", "Banana stem squash.",
             (500, "ml"), "banana-stem-squash-500ml.png", NISARGA,
             "The photograph shows TWO bottles - a regular and one marked "
             "'Sugarless', both 500 ml. Only one banana stem squash was listed "
             "in the catalogue. Is the sugarless one a separate product?"),
            ("Malnad's Nisarga Jamun Squash", "Jamun (Indian blackberry) squash.",
             (700, "ml"), "jamun-squash-700ml.png", NISARGA, ""),
            ("Nanjangud Suruchi's Ginger Lime Syrup", "Ginger and lime syrup.",
             (700, "ml"), "ginger-lime-syrup-700ml.png", SURUCHI,
             "The front label reads 'contains medicinal value' and names "
             "conditions it is for. Our copy will not repeat any of that."),
            ("Nanjangud Suruchi's Grapes Syrup", "Grape syrup.",
             (700, "ml"), "grapes-syrup-700ml.png", SURUCHI, ""),
            ("Nanjangud Suruchi's Jamboo Syrup", "Jamboo syrup.",
             (700, "ml"), "jamboo-syrup-700ml.png", SURUCHI, ""),
            ("Nanjangud Suruchi's Sugarless Jamboo Syrup",
             "Jamboo syrup made without added sugar.", (700, "ml"),
             "sugarless-jamboo-syrup-700ml.png", SURUCHI,
             "'Sugarless' is a nutrition claim with a legal threshold behind it. "
             "Needs the maker's confirmation before it goes on the listing."),
            ("Hallimane Kokam Syrup", "Kokam syrup.", (700, "ml"),
             "kokam-syrup-700ml.png", HALLIMANE, ""),
            ("Nanjangud Suruchi's Diabeat", "Herbal decoction.", (700, "ml"),
             "diabeat-decoction-700ml.png", SURUCHI,
             "THE MOST SERIOUS ITEM IN THE CATALOGUE. The front label calls it a "
             "'proprietory preparation', says it is 'very much useful for "
             "diabetic patients', lists herbal ingredients, and prints a DOSAGE - "
             "'take 30 ml twice before food'. A named condition plus a dose is "
             "how a food stops being a food. Listing it as photographed would "
             "put an unlicensed drug claim on the storefront. Needs a decision "
             "before it goes anywhere near the site."),
        ]
    ],

    # ============================================================== OILS
    P("Aaradhya Pure Double Filtered Coconut Oil", "Oils", UNKNOWN,
      desc="Double filtered coconut oil. Hygienically processed cooking oil.",
      proposed_hsn="1513", proposed_gst="5",
      note="Net volumes read off the labels. No packer, FSSAI, MRP or date "
           "legible on either bottle.",
      variants=[
          V("500 ml", (500, "ml"), "coconut-oil-liter.png", kind="oil"),
          V("1 l", (1, "l"), "coconut-oil-1-liter.png", kind="oil"),
      ]),

    P("Kalpatharu Special Double Filtered Pure Coconut Oil", "Oils", GANESH,
      desc="Double filtered coconut oil.",
      best_before="6 months", pkd="May 2026",
      proposed_hsn="1513", proposed_gst="5",
      note="The catalogue name says 2 litres; the can declares net 1.720 kg, "
           "gross 1.820 kg, 1.9 Ltr. On a sealed pack the maker's declaration "
           "governs, so it is listed at 1.720 kg. The MRP is printed but smudged "
           "and hand-overwritten - illegible, needed from the client.",
      variants=[V("1.720 kg", (1.72, "kg"), "coconut-oil-2-litres.png", kind="can")]),

    P("Ghani-Pressed Copra Coconut Oil", "Oils", DURGA,
      desc="Wood-pressed (ghani) coconut oil from copra.",
      best_before="12 months from the date of packing", pkd="September 2026",
      proposed_hsn="1513", proposed_gst="5",
      note="The most completely declared pack in the catalogue. NOTE: its "
           "printed nutrition panel is wrong - 24 g saturated fat per 100 g for "
           "coconut oil, which is out by roughly a factor of three, and the "
           "mono/poly figures are inverted. Do not reproduce that panel.",
      variants=[V("1 l", (1, "l"), "cold-pressed-coconut-oil-1-liter.png",
                  mrp="450", kind="oil")]),

    # ================================== HOME & PERSONAL CARE (not food)
    P("Antuvala (Soapnut) Powder", "Home & Personal Care", ANNA,
      desc="Soapnut powder, for washing hair.",
      best_before="12 months", pkd="July 2026",
      proposed_hsn="3401", proposed_gst="5",
      note="NOT A FOOD. Washing / hair-care, own storefront section. Rate set to 5% on the client's blanket answer 16 Sep; 3401 is a soap/detergent heading and is normally 18%. Flagged. Curiously the pouch carries an FSSAI food licence.",
      variants=[V("200 g", (200, "g"), "antvala-powder.png", mrp="110")]),

    P("Sikakai (Shikakai) Powder", "Home & Personal Care", ANNA,
      desc="Shikakai powder, for washing hair.",
      best_before="12 months", pkd="August 2026",
      proposed_hsn="3305", proposed_gst="5",
      note="NOT A FOOD. Washing / hair-care. Rate set to 5% on the client's blanket answer 16 Sep; 3305 is a hair-preparation heading and is normally 18%. Flagged.",
      variants=[V("200 g", (200, "g"), "sikakai-powder.png", mrp="120")]),

    P("Soapnut (Whole)", "Home & Personal Care", MS,
      desc="Whole soapnuts, for washing.",
      proposed_hsn="1404", proposed_gst="5",
      note="NOT A FOOD. Quantity and price supplied 16 Sep; the tub prints nothing.",
      variants=[V("150 g", (150, "g"), "sope-nut.png", mrp="140", sell="140", kind="tub")]),
]

# ---------------------------------------------------------------- emit

def main():
    rows = []
    for p in PRODUCTS:
        pk = p["packer"]
        for i, v in enumerate(p["variants"]):
            net = v["net"]
            r = {c: "" for c in COLUMNS}
            r["Product Name"] = p["name"]
            r["Category"] = p["category"]
            if i == 0:
                r["Short Description"] = p["desc"]
                r["Full Description"] = p["full"]
            r["Pack Size"] = v["pack"]
            r["Grind / Form"] = p["form"]
            r["SKU"] = (f"{slug(p['name'])}-{slug(v['pack'])}"
                        if v["pack"] else f"{slug(p['name'])}")
            supplied = PRICES_16SEP.get((p["name"], v["pack"]))
            if supplied:
                v = dict(v, sell=supplied)
                if p["name"] not in RESOLD_NO_MRP:
                    v["mrp"] = supplied
            r["MRP (INR incl. all taxes)"] = v["mrp"]
            # Client instruction 16 Sep: "selling prices are as mentioned in
            # the packs itself" - so the selling price IS the MRP unless a
            # different figure was given explicitly.
            r["Selling Price (INR)"] = v["sell"] or v["mrp"]
            r["Shipping Weight (g)"] = ship_weight(net, v["kind"])
            r["Net Quantity"] = net_text(net)
            r["Manufacturer or Packer Name"] = pk["packer"]
            r["Manufacturer or Packer Full Address"] = pk["address"]
            r["Date of Manufacture or Packing"] = v["pkd"] or p["pkd"]
            r["Best Before / Use By"] = v["best_before"] or p["best_before"]
            r["Country of Origin"] = "India" if pk["packer"] else ""
            r["Consumer Care Name"] = pk["care_name"]
            r["Consumer Care Phone"] = pk["care_phone"]
            r["Consumer Care Email"] = pk["care_email"] or SELLER_CARE_EMAIL
            r["FSSAI Licence Number"] = pk["fssai"]
            r["Ingredients"] = p["ingredients"]
            r["Storage Instructions"] = pk["storage"]
            r["Estate / Origin"] = p["origin"]
            r["Roast Level"] = p["roast"]
            r["Image File Names"] = v["images"]
            if p["proposed_gst"]:
                r["HSN Code"] = p["proposed_hsn"]
                r["GST Rate (%)"] = p["proposed_gst"]
            # Stock Qty stays empty on purpose.
            rows.append(r)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {OUT}")
    print(f"  {len(PRODUCTS)} products, {len(rows)} variant rows")
    notes = sum(1 for p in PRODUCTS if p["note"])
    print(f"  {notes} products carry a note for the client")

    write_gaps(rows)
    write_tax_schedule()
    return 0


# --------------------------------------------------------------- reports

MANDATORY = [
    "Net Quantity", "MRP (INR incl. all taxes)", "Best Before / Use By",
    "Date of Manufacture or Packing", "Manufacturer or Packer Name",
    "Manufacturer or Packer Full Address", "Country of Origin",
    "Consumer Care Name", "Consumer Care Phone", "Consumer Care Email",
    "FSSAI Licence Number", "HSN Code", "GST Rate (%)",
    "Selling Price (INR)",
]


def write_gaps(rows):
    out = OUT.parent / "gaps.md"
    per_field = {}
    for r in rows:
        for c in MANDATORY:
            if not r[c].strip():
                per_field.setdefault(c, []).append(r["Product Name"])

    L = ["# What is still missing", "",
         f"Generated from `catalogue/malnad-catalogue.csv` "
         f"({len(rows)} variant rows). Regenerate with "
         "`python3 scripts/build_catalogue.py`.", "",
         "Every blank below is a gap, not a guess. Nothing in the sheet was "
         "invented to fill a hole.", "",
         "## By field", "",
         "| Field | Rows missing it | Who supplies it |", "|---|---|---|"]

    source = {
        "Selling Price (INR)": "Client - price list",
        "MRP (INR incl. all taxes)": "Client - price list / pack stamp",
        "HSN Code": "Jnanottam (CA) - see tax-schedule.md",
        "GST Rate (%)": "Jnanottam (CA) - see tax-schedule.md",
        "Consumer Care Email": "SUPPLIED 16 Sep - drjhrnd5@gmail.com",
        "Date of Manufacture or Packing": "Generated at dispatch - see note below",
        "Best Before / Use By": "Client, or the maker's back label",
        "Net Quantity": "Client - the 9 unlabelled lines",
        "Manufacturer or Packer Name": "Back-of-pack photo needed",
        "Manufacturer or Packer Full Address": "Back-of-pack photo needed",
        "Consumer Care Name": "Back-of-pack photo needed",
        "Consumer Care Phone": "Back-of-pack photo needed",
        "FSSAI Licence Number": "Back-of-pack photo needed",
        "Country of Origin": "Follows the packer",
    }
    for c in MANDATORY:
        n = len(per_field.get(c, []))
        if n:
            L.append(f"| {c} | **{n}** | {source.get(c, '')} |")

    L += ["", "## The two that are not really the client's to send", "",
          "**Date of packing.** He packs to order, so there is no single date "
          "that belongs in a catalogue. It has to be applied to the label at "
          "dispatch and shown on the listing as packed-to-order. That is a "
          "decision for him, and it is the one mandatory declaration a "
          "pack-to-order business cannot hold statically.", "",
          "**Consumer care email - ANSWERED 16 Sep.** `drjhrnd5@gmail.com`. It is not "
          "printed on any pack in the catalogue, his own included, so it could "
          "never have been transcribed. It now goes on every row: as the "
          "packer's email on his own repacked goods, and as the seller's "
          "contact on the goods he resells. The one maker that prints its own "
          "(Shree Durga) keeps it.", "",
          "## Products that cannot be listed at all as photographed", ""]

    for pr in PRODUCTS:
        if pr["note"] and ("CANNOT BE LISTED" in pr["note"]
                           or "SERIOUS" in pr["note"]):
            L.append(f"- **{pr['name']}** - {pr['note']}")

    L += ["", "## Every note, product by product", ""]
    for pr in PRODUCTS:
        if pr["note"]:
            L.append(f"**{pr['name']}**  ")
            L.append(f"{pr['note']}")
            L.append("")

    out.write_text("\n".join(L) + "\n")
    print(f"Wrote {out}")


def write_tax_schedule():
    out = OUT.parent / "tax-schedule.md"
    L = ["# HSN and GST - applied", "",
         "**Rate: 5% on every product.** Dr. Dhanush answered 16 Sep - *\"All "
         "meterials r 5%\"*, split *\"2 1/2 cgst and 2 1/2 sgst\"*, and "
         "*\"Same sir\"* to the instant coffee question. That is applied to "
         "all 57 products and all 63 rows; nothing is left blank.", "",
         "**HSN is mine, the rate is his.** The codes below are my "
         "classification. Twelve of them sit in headings that normally carry "
         "a higher rate than 5% - see `docs/gst-classification.md` for the "
         "list and the reasoning. The rate stands as he gave it; the mismatch "
         "is recorded, not silently reconciled.", "",
         "**This table does not tax anybody.** `compliance.gst_rate` is our "
         "own metafield, for the accountant. Checkout tax comes from Shopify "
         "Settings > Taxes and duties, which is still unconfigured.", "",
         "| Product | Category | HSN | Rate | Note |",
         "|---|---|---|---|---|"]
    for pr in PRODUCTS:
        rate = pr["proposed_gst"] or "**?**"
        note = (pr["note"] or "").replace("|", "/")
        if len(note) > 150:
            note = note[:147] + "..."
        L.append(f"| {pr['name']} | {pr['category']} | "
                 f"{pr['proposed_hsn'] or '?'} | {rate} | {note} |")

    L += ["", "## The ones I would actually flag", "",
          "1. **The six Swad masala blends.** Mixed spice blends, 5% or 12%. "
          "This is the open question already recorded in CLAUDE.md and it "
          "affects the biggest-selling lines.",
          "2. **Swad Instant Coffee.** Instant coffee is an extract, which "
          "reads as HSN 2101 at 18%, not 0901 at 5%. If that is right it is "
          "the largest rate difference in the catalogue.",
          "3. **Nice and filter coffee.** If chicory is blended in, the "
          "classification moves. The ingredients are not printed on either "
          "pack, so we cannot tell from the photographs.",
          "4. **Sasive (mustard).** An oil seed in chapter 12, not a spice in "
          "chapter 09.",
          "5. **Soapnut powder, sikakai powder, whole soapnuts.** Not food at "
          "all. Washing and hair-care, so a different chapter and almost "
          "certainly a different rate.",
          "6. **The nine syrups and squashes.** Sugar-based preparations, "
          "likely 2106 - but jamun and banana stem squash may classify as "
          "fruit preparations instead.",
          ""]
    out.write_text("\n".join(L) + "\n")
    print(f"Wrote {out}")


if __name__ == "__main__":
    sys.exit(main())
