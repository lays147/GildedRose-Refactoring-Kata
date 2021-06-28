import pytest
from kata.goods.good_interface import Good
from kata.goods.sulfuras_good import SulfurasdGood


def test_update_quality_of_sulfuras_valid_item(sulfuras_valid_item):
    good = SulfurasdGood(sulfuras_valid_item)
    good.update_quality()

    assert isinstance(good, Good)
    assert sulfuras_valid_item.sell_in == None
    assert sulfuras_valid_item.quality == 80
    assert sulfuras_valid_item.name == "Sulfuras, Hand of Ragnaros"


def test_update_quality_of_sulfuras_invalid_item(sulfuras_invalid_item):
    with pytest.raises(AttributeError) as excinfo:
        SulfurasdGood(sulfuras_invalid_item)
    assert (
        "Error! Sulfuras Good has constant quality of 80 and no sell in date!"
        in str(excinfo.value)
    )
