from inventory import Inventory, NoRoomError, InvalidQuantityError, NoSuchItemError, OutOfStockError

import pytest

@pytest.fixture
def default_inv():
    return Inventory()

@pytest.fixture
def ten_pants_inv():
    inv = Inventory()
    inv.set_stock('Pants', 50.00, 10)
    return inv

def set_stock_helper(inv, name, price, quantity):
    prev_total = inv.total_stock()
    inv.set_stock(name, price, quantity)

    assert inv.items[name]['price'] == price
    assert inv.items[name]['quantity'] == quantity
    assert inv.total_stock() == prev_total + quantity

def remove_stock_helper(inv, name, quantity):
    prev_total = inv.total_stock()
    prev_quantity = inv.items[name]['quantity']
    prev_price = inv.items[name]['price']
    inv.remove_stock(name, quantity)

    assert inv.items[name]['price'] == prev_price
    assert inv.items[name]['quantity'] == prev_quantity - quantity
    assert inv.total_stock() == prev_total - quantity

def test_default_inventory(default_inv):
    assert default_inv.limit == 100
    assert default_inv.total_stock() == 0

def test_ten_pants_inv(ten_pants_inv):
    assert ten_pants_inv.limit == 100
    assert ten_pants_inv.items['Pants']['price'] == 50.00
    assert ten_pants_inv.items['Pants']['quantity'] == 10
    assert ten_pants_inv.total_stock() == 10

def test_set_stock_new_item(ten_pants_inv):
    set_stock_helper(ten_pants_inv, 'Shirt', 25.00, 20)

def test_set_stock_negative(default_inv):
    with pytest.raises(InvalidQuantityError):
        default_inv.set_stock('Pants', 50.00, -2)

    assert default_inv.total_stock() == 0

def test_set_stock_too_many(default_inv):
    set_stock_helper(default_inv, 'Pants', 50.00, 90)

    with pytest.raises(NoRoomError):
        default_inv.set_stock('Shirt', 25.00, 20)

    assert default_inv.total_stock() == 90

def test_remove_stock_available(ten_pants_inv):
    remove_stock_helper(ten_pants_inv, 'Pants', 6)

def test_remove_stock_out_of_stock(ten_pants_inv):
    remove_stock_helper(ten_pants_inv, 'Pants', 10)

    with pytest.raises(OutOfStockError):
        ten_pants_inv.remove_stock('Pants', 1)
    
    assert ten_pants_inv.total_stock() == 0

def test_remove_stock_negative(ten_pants_inv):
    with pytest.raises(InvalidQuantityError):
        ten_pants_inv.remove_stock('Pants', -5)

    assert ten_pants_inv.total_stock() == 10

def test_remove_stock_no_such_item(ten_pants_inv):
    with pytest.raises(NoSuchItemError):
        ten_pants_inv.remove_stock('afdsasdf', 5)

    assert ten_pants_inv.total_stock() == 10
