from inventory import Inventory, NoRoomError, InvalidQuantityError, NoSuchItemError, OutOfStockError

import pytest

def test_default_inventory():
    inv = Inventory()
    assert inv.limit == 100
    assert inv.total_stock() == 0

def test_set_stock_new_item():
    inv = Inventory()
    assert inv.limit == 100
    assert inv.total_stock() == 0

    inv.set_stock('Pants', 50.00, 10)
    assert inv.items['Pants']['price'] == 50.00
    assert inv.items['Pants']['quantity'] == 10
    assert inv.total_stock() == 10

    inv.set_stock('Shirt', 25.00, 20)
    assert inv.items['Shirt']['price'] == 25.00
    assert inv.items['Shirt']['quantity'] == 20
    assert inv.total_stock() == 30

def test_set_stock_negative():
    inv = Inventory()
    assert inv.limit == 100
    assert inv.total_stock() == 0

    with pytest.raises(InvalidQuantityError):
        inv.set_stock('Pants', 50.00, -2)

    assert inv.total_stock() == 0

def test_set_stock_too_many():
    inv = Inventory()
    assert inv.limit == 100
    assert inv.total_stock() == 0

    inv.set_stock('Pants', 50.00, 90)
    assert inv.items['Pants']['price'] == 50.00
    assert inv.items['Pants']['quantity'] == 90
    assert inv.total_stock() == 90

    with pytest.raises(NoRoomError):
        inv.set_stock('Shirt', 25.00, 20)

    assert inv.total_stock() == 90

def test_remove_stock_available():
    inv = Inventory()
    assert inv.limit == 100
    assert inv.total_stock() == 0

    inv.set_stock('Pants', 50.00, 10)
    assert inv.items['Pants']['price'] == 50.00
    assert inv.items['Pants']['quantity'] == 10
    assert inv.total_stock() == 10

    inv.remove_stock('Pants', 6)
    assert inv.items['Pants']['price'] == 50.00
    assert inv.items['Pants']['quantity'] == 4
    assert inv.total_stock() == 4

def test_remove_stock_out_of_stock():
    inv = Inventory()
    assert inv.limit == 100
    assert inv.total_stock() == 0

    inv.set_stock('Pants', 50.00, 10)
    assert inv.items['Pants']['price'] == 50.00
    assert inv.items['Pants']['quantity'] == 10
    assert inv.total_stock() == 10

    inv.remove_stock('Pants', 10)
    assert inv.items['Pants']['price'] == 50.00
    assert inv.items['Pants']['quantity'] == 0
    assert inv.total_stock() == 0

    with pytest.raises(OutOfStockError):
        inv.remove_stock('Pants', 1)
    
    assert inv.total_stock() == 0

def test_remove_stock_negative():
    inv = Inventory()
    assert inv.limit == 100
    assert inv.total_stock() == 0

    inv.set_stock('Pants', 50.00, 10)
    assert inv.items['Pants']['price'] == 50.00
    assert inv.items['Pants']['quantity'] == 10
    assert inv.total_stock() == 10

    with pytest.raises(InvalidQuantityError):
        inv.remove_stock('Pants', -5)

    assert inv.total_stock() == 10

def test_remove_stock_no_such_item():
    inv = Inventory()
    assert inv.limit == 100
    assert inv.total_stock() == 0

    inv.set_stock('Pants', 50.00, 10)
    assert inv.items['Pants']['price'] == 50.00
    assert inv.items['Pants']['quantity'] == 10
    assert inv.total_stock() == 10

    with pytest.raises(NoSuchItemError):
        inv.remove_stock('afdsasdf', 5)

    assert inv.total_stock() == 10
