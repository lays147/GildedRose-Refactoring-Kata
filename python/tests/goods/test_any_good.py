import pytest

from kata.goods.any_good import AnyGood
from kata.goods.good_interface import Good
from kata.item import Item


@pytest.fixture
def any_good_item() -> Item:
    return Item(name="Elixir of the Mongoose", sell_in=10, quality=30)


@pytest.fixture
def any_good_item2() -> Item:
    return Item(name="+5 Dexterity Vest", sell_in=0, quality=30)


def test_update_quality_of_any_good_good_where_sell_item_is_not_passed(any_good_item):
    good = AnyGood(any_good_item)
    good.update_quality()

    assert isinstance(good, Good)
    assert any_good_item.sell_in is 9
    assert any_good_item.quality is 29
    assert any_good_item.name is "Elixir of the Mongoose"


def test_update_quality_of_any_good_good_where_sell_item_is_passed(any_good_item2):
    good = AnyGood(any_good_item2)
    good.update_quality()

    assert isinstance(good, Good)
    assert any_good_item2.sell_in is -1
    assert any_good_item2.quality is 28
    assert any_good_item2.name is "+5 Dexterity Vest"
