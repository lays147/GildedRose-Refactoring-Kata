import pytest

from kata.gilded_rose import GildedRose
from kata.item import Item


@pytest.fixture
def aged_brie_item() -> Item:
    return Item(name="Aged Brie", sell_in=10, quality=30)


@pytest.fixture
def aged_brie_item2() -> Item:
    return Item(name="Aged Brie", sell_in=0, quality=30)


def test_update_quality_for_aged_brie_item_where_sell_item_is_not_passed(
    aged_brie_item,
):
    gilded_rose = GildedRose([aged_brie_item])
    gilded_rose.update_quality()

    assert gilded_rose.items[0].sell_in is 9
    assert gilded_rose.items[0].quality is 31
    assert gilded_rose.items[0].name is "Aged Brie"


def test_update_quality_for_aged_brie_item_where_sell_item_is_passed(aged_brie_item2):
    gilded_rose = GildedRose([aged_brie_item2])
    gilded_rose.update_quality()

    assert gilded_rose.items[0].sell_in is -1
    assert gilded_rose.items[0].quality is 32
    assert gilded_rose.items[0].name is "Aged Brie"
