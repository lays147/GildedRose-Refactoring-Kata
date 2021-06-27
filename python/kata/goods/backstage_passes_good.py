from .good_interface import Good


class BackstagePassesGood(Good):
    def update_quality(self) -> None:
        """
        Backstage Passes
        Rules:
            "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches
            Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
            Quality drops to 0 after the concert
        """
        self._item.sell_in -= 1
        if self._item.sell_in >= 0:
            self._item.quality = min(50, self._item.quality + 1)
            if self._item.sell_in <= 10:
                self._item.quality = min(50, self._item.quality + 1)
            if self._item.sell_in <= 5:
                self._item.quality = min(50, self._item.quality + 1)
        else:
            self._item.quality = 0
