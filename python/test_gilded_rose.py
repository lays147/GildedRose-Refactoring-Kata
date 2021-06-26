# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_gilded_rose_creation(self):
        items = [Item('Aged Brie', 0,0)]
        gilded_rose = GildedRose(items)
        assert isinstance(gilded_rose, GildedRose)
        assert len(gilded_rose.items) is 1

    def test_update_quality_case_one(self):
        """
        [One] 
            Conditions:
                item name is not Aged Brie and is not Backstage
                item has quality > 0
                item name is not Sulfuras
            Result: 
                item quality is decreased by one
        [Two]
            Condition:
                item name is not Sulfuras
            Result:
                item sell_in is decreased by one
        [Three]
            Conditions:
                item sell_in is > 0
            Result:
                item quality remains the same
        
        Test Case:
            item = Item('Item', sell_in = 2, quality = 5)
            [One] -> item.quality = 4
            [Two] -> item.sell_in = 1
            [Three] -> item.quality = 4
        
        Expected Result:
            item.quality == 4
            item.sell_in == 1 
            item.name == Item
        """
        items = [Item(name='Item', sell_in=2, quality = 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality is 4
        assert gilded_rose.items[0].sell_in is 1
        assert gilded_rose.items[0].name is 'Item'

if __name__ == '__main__':
    unittest.main()
