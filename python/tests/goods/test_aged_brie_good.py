from kata.goods.aged_brie_good import AgedBrie
from kata.goods.good_interface import Good


def test_update_quality_of_aged_brie_good_where_sell_item_is_not_passed(aged_brie_item):
    good = AgedBrie(aged_brie_item)
    good.update_quality()

    assert isinstance(good, Good)
    assert aged_brie_item.sell_in == 9
    assert aged_brie_item.quality == 31
    assert aged_brie_item.name == "Aged Brie"


def test_update_quality_of_aged_brie_good_where_sell_item_is_passed(aged_brie_item2):
    good = AgedBrie(aged_brie_item2)
    good.update_quality()

    assert isinstance(good, Good)
    assert aged_brie_item2.sell_in == -1
    assert aged_brie_item2.quality == 32
    assert aged_brie_item2.name == "Aged Brie"
