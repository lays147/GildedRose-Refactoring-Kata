from kata.gilded_rose import GildedRose
from kata.item import Item


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo" == items[0].name


def test_gilded_rose_creation():
    items = [Item("Aged Brie", 0, 0)]
    gilded_rose = GildedRose(items)
    assert isinstance(gilded_rose, GildedRose)
    assert len(gilded_rose.items) is 1
