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

    def test_update_quality_case_two(self):
        """
        [One]
            Conditions:
                item name is not Aged Brie and is not Backstage
                item has quality > 0
                item name is Sulfuras
            Result: 
                item quality remains the same
        [Two]
            Condition:
                item name is Sulfuras
            Result:
                item sell_in remains the same
        [Three]
            Conditions:
                item sell_in is > 0
            Result:
                item quality remains the same
        Test Case:
            item = Item('Sulfuras, Hand of Ragnaros', sell_in = 2, quality = 5)
            [One] -> item.quality = 5
            [Two] -> item.sell_in = 2
            [Three] -> item.quality = 2
        Expected Result:
            item.quality == 5
            item.sell_in == 2 
            item.name == Sulfuras, Hand of Ragnaros
        """
        items = [Item(name='Sulfuras, Hand of Ragnaros', sell_in=-1, quality = 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality is 80
        assert gilded_rose.items[0].sell_in is -1
        assert gilded_rose.items[0].name is 'Sulfuras, Hand of Ragnaros'

    def test_update_quality_case_three(self):
        """
        [One]
            Conditions:
                item name is not Aged Brie and is not Backstage
                item has quality < 0
            Result: 
                item quality remains the same
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
            item = Item('Item', sell_in = 2, quality = -1)
            [One] -> item.quality = -1
            [Two] -> item.sell_in = 1
            [Three] -> item.quality = -1
        Expected Result:
            item.quality == -1
            item.sell_in == -1 
            item.name == Item
        """
        items = [Item(name='Item', sell_in=2, quality = -1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality is -1
        assert gilded_rose.items[0].sell_in is 1
        assert gilded_rose.items[0].name is 'Item'

    def test_update_quality_case_four(self):
        """
        [One]
            Conditions:
                item name is Aged Brie or is Backstage
                item has quality > 50
            Result: 
                item quality remains the same
        [Two]
            Condition:
                item name is not Sulfuras
            Result:
                item sell_in is decreased by one
        [Three]
            Conditions:
                item sell_in > 0
            Result:
                item quality remains the same
        Test Case:
            item = Item('Aged Brie', sell_in = 2, quality = 50)
            [One] -> item.quality = 50
            [Two] -> item.sell_in = 1
            [Three] -> item.quality = 50
        Expected Result:
            item.quality == 50
            item.sell_in == 1 
            item.name == Aged Brie
        """
        items = [Item(name='Aged Brie', sell_in=2, quality = 50), Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=2, quality = 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality is 50
        assert gilded_rose.items[0].sell_in is 1
        assert gilded_rose.items[0].name is 'Aged Brie'
        assert gilded_rose.items[1].quality is 50
        assert gilded_rose.items[1].sell_in is 1
        assert gilded_rose.items[1].name is 'Backstage passes to a TAFKAL80ETC concert'
    
    def test_update_quality_case_five(self):
        """
        [One]
            Conditions:
                item name is Aged Brie
                item has quality < 50
            Result: 
                item quality increases by one
        [Two]
            Condition:
                item name is not Sulfuras
            Result:
                item sell_in is decreased by one
        [Three]
            Conditions:
                item sell_in > 0
            Result:
                item quality remains the same
        Test Case:
            item = Item('Aged Brie', sell_in = 2, quality = 40)
            [One] -> item.quality = 41
            [Two] -> item.sell_in = 1
            [Three] -> item.quality = 41
        Expected Result:
            item.quality == 41
            item.sell_in == 1
            item.name == Aged Brie
        """
        items = [Item(name='Aged Brie', sell_in=2, quality = 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert gilded_rose.items[0].quality is 41
        assert gilded_rose.items[0].sell_in is 1
        assert gilded_rose.items[0].name is 'Aged Brie'

if __name__ == '__main__':
    unittest.main()
