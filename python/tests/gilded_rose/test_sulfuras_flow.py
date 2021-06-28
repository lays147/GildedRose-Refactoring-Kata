import pytest

from kata.gilded_rose import GildedRose
from kata.item import Item


def test_update_quality_for_sulfuras_valid_item(
    sulfuras_valid_item,
):
    gilded_rose = GildedRose([sulfuras_valid_item])
    gilded_rose.update_quality()

    assert gilded_rose.items[0].sell_in == None
    assert gilded_rose.items[0].quality == 80
    assert gilded_rose.items[0].name == "Sulfuras, Hand of Ragnaros"


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
