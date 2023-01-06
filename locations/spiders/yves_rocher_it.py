from locations.storefinders.uberall import UberallSpider


class YvesRocherItSpider(UberallSpider):
    name = "yves_rocher_it"
    item_attributes = {
        "brand": "Yves Rocher",
        "brand_wikidata": "Q1477321",
    }
    key = "HLGRPp968JZaR0D235dXJa5fMRPHuA"
