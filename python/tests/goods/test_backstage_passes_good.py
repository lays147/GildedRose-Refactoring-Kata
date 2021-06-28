from kata.goods.backstage_passes_good import BackstagePassesGood
from kata.goods.good_interface import Good


def test_update_quality_of_backstage_good_where_sell_item_is_bigger_than_10(
    backstage_passes_item,
):
    good = BackstagePassesGood(backstage_passes_item)
    good.update_quality()

    assert isinstance(good, Good)
    assert backstage_passes_item.sell_in == 14
    assert backstage_passes_item.quality == 31
    assert backstage_passes_item.name == "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_of_backstage_good_where_sell_item_is_less_than_10(
    backstage_passes_item2,
):
    good = BackstagePassesGood(backstage_passes_item2)
    good.update_quality()

    assert isinstance(good, Good)
    assert backstage_passes_item2.sell_in == 8
    assert backstage_passes_item2.quality == 32
    assert backstage_passes_item2.name == "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_of_backstage_good_where_sell_item_is_less_than_5(
    backstage_passes_item3,
):
    good = BackstagePassesGood(backstage_passes_item3)
    good.update_quality()

    assert isinstance(good, Good)
    assert backstage_passes_item3.sell_in == 3
    assert backstage_passes_item3.quality == 33
    assert backstage_passes_item3.name == "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_of_backstage_good_where_sell_item_is_passed(
    backstage_passes_item4,
):
    good = BackstagePassesGood(backstage_passes_item4)
    good.update_quality()

    assert isinstance(good, Good)
    assert backstage_passes_item4.sell_in == -1
    assert backstage_passes_item4.quality == 0
    assert backstage_passes_item4.name == "Backstage passes to a TAFKAL80ETC concert"
