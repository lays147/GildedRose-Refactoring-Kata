import pytest

from kata.goods.aged_brie_good import AgedBrie
from kata.goods.good_interface import Good
from kata.item import Item


@pytest.fixture
def aged_brie_item() -> Item:
    return Item(name="Aged Brie", sell_in=10, quality=30)


@pytest.fixture
def aged_brie_item2() -> Item:
    return Item(name="Aged Brie", sell_in=0, quality=30)


def test_update_quality_of_aged_brie_good_where_sell_item_is_not_passed(aged_brie_item):
    good = AgedBrie(aged_brie_item)
    good.update_quality()

    assert isinstance(good, Good)
    assert aged_brie_item.sell_in is 9
    assert aged_brie_item.quality is 31
    assert aged_brie_item.name is "Aged Brie"


def test_update_quality_of_aged_brie_good_where_sell_item_is_passed(aged_brie_item2):
    good = AgedBrie(aged_brie_item2)
    good.update_quality()

    assert isinstance(good, Good)
    assert aged_brie_item2.sell_in is -1
    assert aged_brie_item2.quality is 32
    assert aged_brie_item2.name is "Aged Brie"
