import pytest

from kata.item import Item


# Cojured Fixtures
@pytest.fixture
def conjured_item() -> Item:
    return Item(name="Conjured Mana Cake", sell_in=10, quality=30)


@pytest.fixture
def conjured_item2() -> Item:
    return Item(name="Conjured Mana Cake", sell_in=0, quality=30)


# Aged Brie Fixtures
@pytest.fixture
def aged_brie_item() -> Item:
    return Item(name="Aged Brie", sell_in=10, quality=30)


@pytest.fixture
def aged_brie_item2() -> Item:
    return Item(name="Aged Brie", sell_in=0, quality=30)


# Any Fixtures
@pytest.fixture
def any_good_item() -> Item:
    return Item(name="Elixir of the Mongoose", sell_in=10, quality=30)


@pytest.fixture
def any_good_item2() -> Item:
    return Item(name="+5 Dexterity Vest", sell_in=0, quality=30)


# Backstage Fixtures
@pytest.fixture
def backstage_passes_item() -> Item:
    return Item(
        name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=30
    )


@pytest.fixture
def backstage_passes_item2() -> Item:
    return Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=30)


@pytest.fixture
def backstage_passes_item3() -> Item:
    return Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=30)


@pytest.fixture
def backstage_passes_item4() -> Item:
    return Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=30)


# Sulfuras Fixtures
@pytest.fixture
def sulfuras_valid_item() -> Item:
    return Item(name="Sulfuras, Hand of Ragnaros", sell_in=None, quality=80)


@pytest.fixture
def sulfuras_invalid_item() -> Item:
    return Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=80)
