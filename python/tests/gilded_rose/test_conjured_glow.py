import pytest

from kata.gilded_rose import GildedRose
from kata.item import Item


@pytest.fixture
def conjured_item() -> Item:
    return Item(name="Conjured Mana Cake", sell_in=10, quality=30)


@pytest.fixture
def conjured_item2() -> Item:
    return Item(name="Conjured Mana Cake", sell_in=0, quality=30)


def test_update_quality_for_conjured_item_where_sell_item_is_not_passed(conjured_item):
    gilded_rose = GildedRose([conjured_item])
    gilded_rose.update_quality()

    assert gilded_rose.items[0].sell_in is 9
    assert gilded_rose.items[0].quality is 28
    assert gilded_rose.items[0].name is "Conjured Mana Cake"


def test_update_quality_for_conjured_item_where_sell_item_is_passed(conjured_item2):
    gilded_rose = GildedRose([conjured_item2])
    gilded_rose.update_quality()

    assert gilded_rose.items[0].sell_in is -1
    assert gilded_rose.items[0].quality is 26
    assert gilded_rose.items[0].name is "Conjured Mana Cake"
