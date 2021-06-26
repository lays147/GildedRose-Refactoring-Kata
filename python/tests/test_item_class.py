import unittest

from kata.gilded_rose import Item

class ItemTest(unittest.TestCase):

    def test_create_item(self):
        item = Item(name='Aged Brie', sell_in=10, quality=1)
        assert isinstance(item, Item)
        assert item.name == 'Aged Brie'
        assert item.sell_in == 10
        assert item.quality ==1

    def test_repr_item(self):
        item = repr(Item(name='Aged Brie', sell_in=10, quality=1))
        assert item == 'Aged Brie, 10, 1'
