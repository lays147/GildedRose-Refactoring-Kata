import pytest

from kata.goods.good_interface import Good
from kata.goods.sulfuras_good import SulfurasdGood
from kata.item import Item


@pytest.fixture
def sulfuras_valid_item() -> Item:
    return Item(name="Sulfuras, Hand of Ragnaros", sell_in=None, quality=80)


@pytest.fixture
def sulfuras_invalid_item() -> Item:
    return Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=80)


def test_update_quality_of_sulfuras_valid_item(sulfuras_valid_item):
    good = SulfurasdGood(sulfuras_valid_item)
    good.update_quality()

    assert isinstance(good, Good)
    assert sulfuras_valid_item.sell_in is None
    assert sulfuras_valid_item.quality is 80
    assert sulfuras_valid_item.name is "Sulfuras, Hand of Ragnaros"


def test_update_quality_of_sulfuras_invalid_item(sulfuras_invalid_item):
    with pytest.raises(AttributeError) as excinfo:
        good = SulfurasdGood(sulfuras_invalid_item)
    assert (
        "Error! Sulfuras Good has constant quality of 80 and no sell in date!"
        in str(excinfo.value)
    )
