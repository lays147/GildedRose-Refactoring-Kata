from kata.goods.any_good import AnyGood
from kata.goods.good_interface import Good


def test_update_quality_of_any_good_good_where_sell_item_is_not_passed(any_good_item):
    good = AnyGood(any_good_item)
    good.update_quality()

    assert isinstance(good, Good)
    assert any_good_item.sell_in == 9
    assert any_good_item.quality == 29
    assert any_good_item.name == "Elixir of the Mongoose"


def test_update_quality_of_any_good_good_where_sell_item_is_passed(any_good_item2):
    good = AnyGood(any_good_item2)
    good.update_quality()

    assert isinstance(good, Good)
    assert any_good_item2.sell_in == -1
    assert any_good_item2.quality == 28
    assert any_good_item2.name == "+5 Dexterity Vest"
