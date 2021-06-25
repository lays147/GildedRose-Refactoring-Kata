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

        
if __name__ == '__main__':
    unittest.main()
