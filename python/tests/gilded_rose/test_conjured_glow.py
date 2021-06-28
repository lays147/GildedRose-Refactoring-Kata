import pytest

from kata.gilded_rose import GildedRose
from kata.item import Item


def test_update_quality_for_conjured_item_where_sell_item_is_not_passed(conjured_item):
    gilded_rose = GildedRose([conjured_item])
    gilded_rose.update_quality()

    assert gilded_rose.items[0].sell_in == 9
    assert gilded_rose.items[0].quality == 28
    assert gilded_rose.items[0].name == "Conjured Mana Cake"


def test_update_quality_for_conjured_item_where_sell_item_is_passed(conjured_item2):
    gilded_rose = GildedRose([conjured_item2])
    gilded_rose.update_quality()

    assert gilded_rose.items[0].sell_in == -1
    assert gilded_rose.items[0].quality == 26
    assert gilded_rose.items[0].name == "Conjured Mana Cake"
