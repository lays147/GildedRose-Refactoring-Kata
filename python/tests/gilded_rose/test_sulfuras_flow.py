import pytest

from kata.gilded_rose import GildedRose
from kata.item import Item


@pytest.fixture
def sulfuras_valid_item() -> Item:
    return Item(name="Sulfuras, Hand of Ragnaros", sell_in=None, quality=80)


@pytest.fixture
def sulfuras_invalid_item() -> Item:
    return Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=80)


def test_update_quality_for_sulfuras_valid_item(
    sulfuras_valid_item,
):
    gilded_rose = GildedRose([sulfuras_valid_item])
    gilded_rose.update_quality()

    assert gilded_rose.items[0].sell_in is None
    assert gilded_rose.items[0].quality is 80
    assert gilded_rose.items[0].name is "Sulfuras, Hand of Ragnaros"


def test_update_quality_for_sulfuras_invalid_item(
    sulfuras_invalid_item,
):
    with pytest.raises(AttributeError) as excinfo:
        gilded_rose = GildedRose([sulfuras_invalid_item])
        gilded_rose.update_quality()
    assert (
        "Error! Sulfuras Good has constant quality of 80 and no sell in date!"
        in str(excinfo.value)
    )
