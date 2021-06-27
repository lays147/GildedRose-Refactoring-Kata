import pytest

from kata.goods.backstage_passes_good import BackstagePassesGood
from kata.goods.good_interface import Good
from kata.item import Item


@pytest.fixture
def backstage_passes_item() -> Item:
    return Item(
        name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=30
    )


@pytest.fixture
def backstage_passes_item2() -> Item:
    return Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=30)


@pytest.fixture
def backstage_passes_item3() -> Item:
    return Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=30)


@pytest.fixture
def backstage_passes_item4() -> Item:
    return Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=30)


def test_update_quality_of_backstage_good_where_sell_item_is_bigger_than_10(
    backstage_passes_item,
):
    good = BackstagePassesGood(backstage_passes_item)
    good.update_quality()

    assert isinstance(good, Good)
    assert backstage_passes_item.sell_in is 14
    assert backstage_passes_item.quality is 31
    assert backstage_passes_item.name is "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_of_backstage_good_where_sell_item_is_less_than_10(
    backstage_passes_item2,
):
    good = BackstagePassesGood(backstage_passes_item2)
    good.update_quality()

    assert isinstance(good, Good)
    assert backstage_passes_item2.sell_in is 8
    assert backstage_passes_item2.quality is 32
    assert backstage_passes_item2.name is "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_of_backstage_good_where_sell_item_is_less_than_5(
    backstage_passes_item3,
):
    good = BackstagePassesGood(backstage_passes_item3)
    good.update_quality()

    assert isinstance(good, Good)
    assert backstage_passes_item3.sell_in is 3
    assert backstage_passes_item3.quality is 33
    assert backstage_passes_item3.name is "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_of_backstage_good_where_sell_item_is_passed(
    backstage_passes_item4,
):
    good = BackstagePassesGood(backstage_passes_item4)
    good.update_quality()

    assert isinstance(good, Good)
    assert backstage_passes_item4.sell_in is -1
    assert backstage_passes_item4.quality is 0
    assert backstage_passes_item4.name is "Backstage passes to a TAFKAL80ETC concert"
