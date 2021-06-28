from kata.gilded_rose import GildedRose


def test_update_quality_of_backstage_good_where_sell_item_is_bigger_than_10(
    backstage_passes_item,
):
    good = GildedRose([backstage_passes_item])
    good.update_quality()

    assert good.items[0].sell_in == 14
    assert good.items[0].quality == 31
    assert good.items[0].name == "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_of_backstage_good_where_sell_item_is_less_than_10(
    backstage_passes_item2,
):
    good = GildedRose([backstage_passes_item2])
    good.update_quality()

    assert good.items[0].sell_in == 8
    assert good.items[0].quality == 32
    assert good.items[0].name == "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_of_backstage_good_where_sell_item_is_less_than_5(
    backstage_passes_item3,
):
    good = GildedRose([backstage_passes_item3])
    good.update_quality()

    assert good.items[0].sell_in == 3
    assert good.items[0].quality == 33
    assert good.items[0].name == "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_of_backstage_good_where_sell_item_is_passed(
    backstage_passes_item4,
):
    good = GildedRose([backstage_passes_item4])
    good.update_quality()

    assert good.items[0].sell_in == -1
    assert good.items[0].quality == 0
    assert good.items[0].name == "Backstage passes to a TAFKAL80ETC concert"
