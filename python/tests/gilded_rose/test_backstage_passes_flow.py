import pytest

from kata.gilded_rose import GildedRose
from kata.goods.backstage_passes_good import BackstagePassesGood
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
    good = GildedRose([backstage_passes_item])
    good.update_quality()

    assert good.items[0].sell_in is 14
    assert good.items[0].quality is 31
    assert good.items[0].name is "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_of_backstage_good_where_sell_item_is_less_than_10(
    backstage_passes_item2,
):
    good = GildedRose([backstage_passes_item2])
    good.update_quality()

    assert good.items[0].sell_in is 8
    assert good.items[0].quality is 32
    assert good.items[0].name is "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_of_backstage_good_where_sell_item_is_less_than_5(
    backstage_passes_item3,
):
    good = GildedRose([backstage_passes_item3])
    good.update_quality()

    assert good.items[0].sell_in is 3
    assert good.items[0].quality is 33
    assert good.items[0].name is "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_of_backstage_good_where_sell_item_is_passed(
    backstage_passes_item4,
):
    good = GildedRose([backstage_passes_item4])
    good.update_quality()

    assert good.items[0].sell_in is -1
    assert good.items[0].quality is 0
    assert good.items[0].name is "Backstage passes to a TAFKAL80ETC concert"
