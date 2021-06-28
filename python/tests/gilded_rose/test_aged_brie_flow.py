from kata.gilded_rose import GildedRose


def test_update_quality_for_aged_brie_item_where_sell_item_is_not_passed(
    aged_brie_item,
):
    gilded_rose = GildedRose([aged_brie_item])
    gilded_rose.update_quality()

    assert gilded_rose.items[0].sell_in == 9
    assert gilded_rose.items[0].quality == 31
    assert gilded_rose.items[0].name == "Aged Brie"


def test_update_quality_for_aged_brie_item_where_sell_item_is_passed(aged_brie_item2):
    gilded_rose = GildedRose([aged_brie_item2])
    gilded_rose.update_quality()

    assert gilded_rose.items[0].sell_in == -1
    assert gilded_rose.items[0].quality == 32
    assert gilded_rose.items[0].name == "Aged Brie"
