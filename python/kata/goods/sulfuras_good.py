from ..item import Item
from .good_interface import Good


class SulfurasdGood(Good):
    def __init__(
        self, item: Item(name="Sulfuras, Hand of Ragnaros", sell_in=None, quality=80)
    ) -> None:
        if item.quality != 80 or item.sell_in != None:
            raise AttributeError(
                "Error! Sulfuras Good has constant quality of 80 and no sell in date!"
            )
        self._item = item

    def update_quality(self) -> None:
        """
        Sulfuras Good
        Rules:
            "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
            Just for clarification, an item can never have its Quality increase above 50, however "Sulfuras" is a
            legendary item and as such its Quality is 80 and it never alters.
        """
        pass
