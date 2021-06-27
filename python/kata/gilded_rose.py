from .goods.aged_brie_good import AgedBrie
from .goods.backstage_passes_good import BackstagePassesGood
from .goods.conjured_good import ConjuredGood
from .goods.goods import Goods
from .goods.sulfuras_good import SulfurasdGood


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == Goods.CONJURED.value:
                ConjuredGood(item).update_quality()
                continue
            if item.name == Goods.SULFURAs.value:
                SulfurasdGood(item).update_quality()
                continue
            if item.name == Goods.AGED_BRIE.value:
                AgedBrie(item).update_quality()
                continue
            if item.name == Goods.BACKSTAGE.value:
                BackstagePassesGood(item).update_quality()
                continue
            if (
                item.name != "Aged Brie"
                and item.name != "Backstage passes to a TAFKAL80ETC concert"
            ):
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
