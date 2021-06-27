import pytest

from kata.goods.conjured_good import ConjuredGood
from kata.goods.good_interface import Good
from kata.item import Item


@pytest.fixture
def conjured_item() -> Item:
    return Item(name="Conjured Mana Cake", sell_in=10, quality=30)


@pytest.fixture
def conjured_item2() -> Item:
    return Item(name="Conjured Mana Cake", sell_in=0, quality=30)


def test_update_quality_of_conjured_good_where_sell_item_is_not_passed(conjured_item):
    good = ConjuredGood(conjured_item)
    good.update_quality()

    assert isinstance(good, Good)
    assert conjured_item.sell_in is 9
    assert conjured_item.quality is 28
    assert conjured_item.name is "Conjured Mana Cake"


def test_update_quality_of_conjured_good_where_sell_item_is_passed(conjured_item2):
    good = ConjuredGood(conjured_item2)
    good.update_quality()

    assert isinstance(good, Good)
    assert conjured_item2.sell_in is -1
    assert conjured_item2.quality is 26
    assert conjured_item2.name is "Conjured Mana Cake"
