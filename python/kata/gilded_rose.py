from typing import List

from .goods.aged_brie_good import AgedBrie
from .goods.any_good import AnyGood
from .goods.backstage_passes_good import BackstagePassesGood
from .goods.conjured_good import ConjuredGood
from .goods.goods import Goods
from .goods.sulfuras_good import SulfurasdGood
from .item import Item


class GildedRose:
    def __init__(self, items: List[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            if item.name == Goods.CONJURED.value:
                ConjuredGood(item).update_quality()
            elif item.name == Goods.SULFURAs.value:
                SulfurasdGood(item).update_quality()
            elif item.name == Goods.AGED_BRIE.value:
                AgedBrie(item).update_quality()
            elif item.name == Goods.BACKSTAGE.value:
                BackstagePassesGood(item).update_quality()
            else:
                AnyGood(item).update_quality()
