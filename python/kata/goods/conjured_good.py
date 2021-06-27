from ..item import Item
from .good_interface import Good


class ConjuredGood(Good):
    def update_quality(self) -> None:
        """
        Conjured Good
        Rules:
            Conjured items degrade in Quality twice as fast as normal items
            Once the sell by date has passed, Quality degrades twice as fast
        """
        self._item.sell_in -= 1
        if self._item.sell_in >= 0:
            self._item.quality = max(0, self._item.quality - 2)
        else:
            self._item.quality = max(0, self._item.quality - 4)
