from .good_interface import Good


class AnyGood(Good):
    def update_quality(self) -> None:
        """
        Any Good
        Rules:
            Once the sell by date has passed, Quality degrades twice as fast
        """
        self._item.sell_in -= 1
        if self._item.sell_in >= 0:
            self._item.quality = min(50, self._item.quality - 1)
        else:
            self._item.quality = min(50, self._item.quality - 2)
