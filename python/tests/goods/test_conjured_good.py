from kata.goods.conjured_good import ConjuredGood
from kata.goods.good_interface import Good


def test_update_quality_of_conjured_good_where_sell_item_is_not_passed(conjured_item):
    good = ConjuredGood(conjured_item)
    good.update_quality()

    assert isinstance(good, Good)
    assert conjured_item.sell_in == 9
    assert conjured_item.quality == 28
    assert conjured_item.name == "Conjured Mana Cake"


def test_update_quality_of_conjured_good_where_sell_item_is_passed(conjured_item2):
    good = ConjuredGood(conjured_item2)
    good.update_quality()

    assert isinstance(good, Good)
    assert conjured_item2.sell_in == -1
    assert conjured_item2.quality == 26
    assert conjured_item2.name == "Conjured Mana Cake"
