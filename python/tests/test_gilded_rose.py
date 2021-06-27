from kata.gilded_rose import Item, GildedRose


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


def test_update_quality_case_one():
    """
    [One]
        Conditions:
            item name is not Aged Brie and is not Backstage
            item has quality > 0
            item name is not Sulfuras
        Result:
            item quality is decreased by one
    [Two]
        Condition:
            item name is not Sulfuras
        Result:
            item sell_in is decreased by one
    [Three]
        Conditions:
            item sell_in is > 0
        Result:
            item quality remains the same

    Test Case:
        item = Item('Item', sell_in = 2, quality = 5)
        [One] -> item.quality = 4
        [Two] -> item.sell_in = 1
        [Three] -> item.quality = 4

    Expected Result:
        item.quality == 4
        item.sell_in == 1
        item.name == Item
    """
    items = [Item(name="Item", sell_in=2, quality=5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality is 4
    assert gilded_rose.items[0].sell_in is 1
    assert gilded_rose.items[0].name is "Item"


def test_update_quality_case_two():
    """
    [One]
        Conditions:
            item name is not Aged Brie and is not Backstage
            item has quality > 0
            item name is Sulfuras
        Result:
            item quality remains the same
    [Two]
        Condition:
            item name is Sulfuras
        Result:
            item sell_in remains the same
    [Three]
        Conditions:
            item sell_in is > 0
        Result:
            item quality remains the same
    Test Case:
        item = Item('Sulfuras, Hand of Ragnaros', sell_in = 2, quality = 5)
        [One] -> item.quality = 5
        [Two] -> item.sell_in = 2
        [Three] -> item.quality = 2
    Expected Result:
        item.quality == 5
        item.sell_in == 2
        item.name == Sulfuras, Hand of Ragnaros
    """
    items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality is 80
    assert gilded_rose.items[0].sell_in is -1
    assert gilded_rose.items[0].name is "Sulfuras, Hand of Ragnaros"


def test_update_quality_case_three():
    """
    [One]
        Conditions:
            item name is not Aged Brie and is not Backstage
            item has quality < 0
        Result:
            item quality remains the same
    [Two]
        Condition:
            item name is not Sulfuras
        Result:
            item sell_in is decreased by one
    [Three]
        Conditions:
            item sell_in is > 0
        Result:
            item quality remains the same
    Test Case:
        item = Item('Item', sell_in = 2, quality = -1)
        [One] -> item.quality = -1
        [Two] -> item.sell_in = 1
        [Three] -> item.quality = -1
    Expected Result:
        item.quality == -1
        item.sell_in == -1
        item.name == Item
    """
    items = [Item(name="Item", sell_in=2, quality=-1)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality is -1
    assert gilded_rose.items[0].sell_in is 1
    assert gilded_rose.items[0].name is "Item"


def test_update_quality_case_four():
    """
    [One]
        Conditions:
            item name is Aged Brie or is Backstage
            item has quality > 50
        Result:
            item quality remains the same
    [Two]
        Condition:
            item name is not Sulfuras
        Result:
            item sell_in is decreased by one
    [Three]
        Conditions:
            item sell_in > 0
        Result:
            item quality remains the same
    Test Case:
        item = Item('Aged Brie', sell_in = 2, quality = 50)
        [One] -> item.quality = 50
        [Two] -> item.sell_in = 1
        [Three] -> item.quality = 50
    Expected Result:
        item.quality == 50
        item.sell_in == 1
        item.name == Aged Brie
    """
    items = [
        Item(name="Aged Brie", sell_in=2, quality=50),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=2, quality=50),
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality is 50
    assert gilded_rose.items[0].sell_in is 1
    assert gilded_rose.items[0].name is "Aged Brie"
    assert gilded_rose.items[1].quality is 50
    assert gilded_rose.items[1].sell_in is 1
    assert gilded_rose.items[1].name is "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_case_five():
    """
    [One]
        Conditions:
            item name is Aged Brie
            item has quality < 50
        Result:
            item quality increases by one
    [Two]
        Condition:
            item name is not Sulfuras
        Result:
            item sell_in is decreased by one
    [Three]
        Conditions:
            item sell_in > 0
        Result:
            item quality remains the same
    Test Case:
        item = Item('Aged Brie', sell_in = 2, quality = 40)
        [One] -> item.quality = 41
        [Two] -> item.sell_in = 1
        [Three] -> item.quality = 41
    Expected Result:
        item.quality == 41
        item.sell_in == 1
        item.name == Aged Brie
    """
    items = [Item(name="Aged Brie", sell_in=2, quality=40)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality is 41
    assert gilded_rose.items[0].sell_in is 1
    assert gilded_rose.items[0].name is "Aged Brie"


def test_update_quality_case_six():
    """
    [One]
        Conditions:
            item name is Backstage
            item has quality < 50
            item name is Backstage
            item sell_in > 11
        Result:
            item quality is increased by one
    [Two]
        Condition:
            item name is not Sulfuras
        Result:
            item sell_in is decreased by one
    [Three]
        Conditions:
            item sell_in > 0
        Result:
            item quality remains the same
    Test Case:
        item = Item('Backstage passes to a TAFKAL80ETC concert', sell_in = 15, quality = 40)
        [One] -> item.quality = 41
        [Two] -> item.sell_in = 14
        [Three] -> item.quality = 41
    Expected Result:
        item.quality == 41
        item.sell_in == 14
        item.name == Backstage passes to a TAFKAL80ETC concert
    """
    items = [
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=40)
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality is 41
    assert gilded_rose.items[0].sell_in is 14
    assert gilded_rose.items[0].name is "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_case_seven():
    """
    [One]
        Conditions:
            item name is Backstage
            item has quality < 50 (1)
            item name is Backstage
            item sell_in is between 6 and 11 (2)
        Result:
            (1) item quality is increased by one
            (2) item quality is increased by one
    [Two]
        Condition:
            item name is not Sulfuras
        Result:
            item sell_in is decreased by one
    [Three]
        Conditions:
            item sell_in > 0
        Result:
            item quality remains the same
    Test Case:
        item = Item('Backstage passes to a TAFKAL80ETC concert', sell_in = 8, quality = 40)
        [One] -> item.quality = 42
        [Two] -> item.sell_in = 7
        [Three] -> item.quality = 42
    Expected Result:
        item.quality == 42
        item.sell_in == 7
        item.name == Backstage passes to a TAFKAL80ETC concert
    """
    items = [
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=40)
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality is 42
    assert gilded_rose.items[0].sell_in is 7
    assert gilded_rose.items[0].name is "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_case_eight():
    """
    [One]
        Conditions:
            item name is Backstage
            item has quality < 50 (1)
            item name is Backstage
            item sell_in is < 11
            item quality < 50 (2)
            item sell_in is < 6
            item quality < (3)
        Result:
            (1) item quality is increased by one
            (2) item quality is increased by one
            (3) item quality is increased by one
    [Two]
        Condition:
            item name is not Sulfuras
        Result:
            item sell_in is decreased by one
    [Three]
        Conditions:
            item sell_in > 0
        Result:
            item quality remains the same
    Test Case:
        item = Item('Backstage passes to a TAFKAL80ETC concert', sell_in = 5, quality = 40)
        [One] -> item.quality = 43
        [Two] -> item.sell_in = 4
        [Three] -> item.quality = 43
    Expected Result:
        item.quality == 43
        item.sell_in == 4
        item.name == Backstage passes to a TAFKAL80ETC concert
    """
    items = [
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=40)
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality is 43
    assert gilded_rose.items[0].sell_in is 4
    assert gilded_rose.items[0].name is "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_case_nine():
    """
    [One]
        Conditions:
            item name is not Aged Brie and is not Backstage
            item has quality > 0
            item name is not Sulfuras
        Result:
            item quality is decreased by one
    [Two]
        Condition:
            item name is not Sulfuras
        Result:
            item sell_in is decreased by one
    [Three]
        Conditions:
            item sell_in is < 0
            item name is not Aged Brie
            item name is not Backstage
            item quality > 0
            item name is not Sulfuras
        Result:
            item quality is decreased by one

    Test Case:
        item = Item('Item', sell_in = 0, quality = 5)
        [One] -> item.quality = 4
        [Two] -> item.sell_in = -1
        [Three] -> item.quality = 3

    Expected Result:
        item.quality == 3
        item.sell_in == -1
        item.name == Item
    """
    items = [Item(name="Item", sell_in=0, quality=5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality is 3
    assert gilded_rose.items[0].sell_in is -1
    assert gilded_rose.items[0].name is "Item"


def test_update_quality_case_ten():
    """
    [One]
        Conditions:
            item name is not Aged Brie and is not Backstage
            item has quality > 0
            item name is Sulfuras
        Result:
            item quality remains the same
    [Two]
        Condition:
            item name is Sulfuras
        Result:
            item sell_in remains the same
    [Three]
        Conditions:
            item sell_in is < 0
            item name is not Aged Brie
            item name is not Backstage
            item quality > 0
            item name is Sulfuras
        Result:
            item quality remains the same

    Test Case:
        item = Item('Sulfuras, Hand of Ragnaros', sell_in = -1, quality = 80)
        [One] -> item.quality = 80
        [Two] -> item.sell_in = -1
        [Three] -> item.quality = 80

    Expected Result:
        item.quality == 80
        item.sell_in == -1
        item.name == Sulfuras, Hand of Ragnaros
    """
    items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality is 80
    assert gilded_rose.items[0].sell_in is -1
    assert gilded_rose.items[0].name is "Sulfuras, Hand of Ragnaros"


def test_update_quality_case_eleven():
    """
    [One]
        Conditions:
            item name is not Aged Brie and is not Backstage
            item has quality < 0
        Result:
            item quality remains the same
    [Two]
        Condition:
            item name is not Sulfuras
        Result:
            item sell_in is decreased by one
    [Three]
        Conditions:
            item sell_in is < 0
            item name is not Aged Brie
            item name is not Backstage
            item quality < 0
        Result:
            item quality remains the same

    Test Case:
        item = Item('Item', sell_in = 0, quality = -1)
        [One] -> item.quality = -1
        [Two] -> item.sell_in = -2
        [Three] -> item.quality = -1

    Expected Result:
        item.quality == -1
        item.sell_in == -2
        item.name == Item
    """
    items = [Item(name="Item", sell_in=-1, quality=-1)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality is -1
    assert gilded_rose.items[0].sell_in is -2
    assert gilded_rose.items[0].name is "Item"


def test_update_quality_case_twelve():
    """
    [One]
        Conditions:
            item name is Backstage
            item has quality < 50 (1)
            item name is Backstage
            item sell_in is between 6 and 11 (2)
        Result:
            (1) item quality is increased by one
            (2) item quality is increased by one
    [Two]
        Condition:
            item name is not Sulfuras
        Result:
            item sell_in is decreased by one
    [Three]
        Conditions:
            item sell_in < 0
            item name is not Aged Brie
            item name is Backstage
        Result:
            item quality decreases by item quality value
    Test Case:
        item = Item('Backstage passes to a TAFKAL80ETC concert', sell_in = 0, quality = 40)
        [One] -> item.quality = 42
        [Two] -> item.sell_in = -1
        [Three] -> item.quality = 42
    Expected Result:
        item.quality == 0
        item.sell_in == -1
        item.name == Backstage passes to a TAFKAL80ETC concert
    """
    items = [
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=40)
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality is 0
    assert gilded_rose.items[0].sell_in is -1
    assert gilded_rose.items[0].name is "Backstage passes to a TAFKAL80ETC concert"


def test_update_quality_case_thirteen():
    """
    [One]
        Conditions:
            item name is Aged Brie
            item has quality < 50
        Result:
            item quality increases by one
    [Two]
        Condition:
            item name is not Sulfuras
        Result:
            item sell_in is decreased by one
    [Three]
        Conditions:
            item sell_in < 0
            item name is Aged Brie
            item quality < 50
        Result:
            item quality is increased by one
    Test Case:
        item = Item('Aged Brie', sell_in = 0, quality = 40)
        [One] -> item.quality = 41
        [Two] -> item.sell_in = -1
        [Three] -> item.quality = 42
    Expected Result:
        item.quality == 42
        item.sell_in == -1
        item.name == Aged Brie
    """
    items = [Item(name="Aged Brie", sell_in=0, quality=40)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality is 42
    assert gilded_rose.items[0].sell_in is -1
    assert gilded_rose.items[0].name is "Aged Brie"


def test_update_quality_case_fourteen():
    """
    [One]
        Conditions:
            item name is Aged Brie
            item has quality == 50
        Result:
            item quality remains the same
    [Two]
        Condition:
            item name is not Sulfuras
        Result:
            item sell_in is decreased by one
    [Three]
        Conditions:
            item sell_in < 0
            item name is Aged Brie
            item has quality == 50
        Result:
            item quality remains the same
    Test Case:
        item = Item('Aged Brie', sell_in = 0, quality = 50)
        [One] -> item.quality = 50
        [Two] -> item.sell_in = -1
        [Three] -> item.quality = 50
    Expected Result:
        item.quality == 50
        item.sell_in == -1
        item.name == Aged Brie
    """
    items = [Item(name="Aged Brie", sell_in=0, quality=50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality is 50
    assert gilded_rose.items[0].sell_in is -1
    assert gilded_rose.items[0].name is "Aged Brie"
