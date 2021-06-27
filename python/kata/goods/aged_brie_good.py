from .good_interface import Good


class AgedBrie(Good):
    def update_quality(self) -> None:
        """
        Aged Brie Good
        Rules:
            Once the sell by date has passed, Quality degrades twice as fast
            "Aged Brie" actually increases in Quality the older it gets
        """
        self._item.sell_in -= 1
        if self._item.sell_in >= 0:
            self._item.quality = min(50, self._item.quality + 1)
        else:
            self._item.quality = min(50, self._item.quality + 2)
