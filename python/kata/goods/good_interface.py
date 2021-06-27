from abc import ABC, abstractmethod

from ..item import Item


class Good(ABC):
    """
    This class represents an interface for a Good of Gilded Rose
    """

    def __init__(self, item: Item) -> None:
        self._item = item

    # @property
    # def item(self):
    #     return self._item

    # @item.setter
    # def item(self, item: Item) -> None:
    #     self._item = item

    @abstractmethod
    def update_quality(self) -> None:
        pass
