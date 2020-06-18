from inventory import Inventory, NoRoomError, InvalidQuantityError, NoSuchItemError, OutOfStockError

import pytest
from unittest.mock import create_autospec, MagicMock
from http.client import HTTPConnection
import json

@pytest.fixture
def default_inv():
    return Inventory()

@pytest.fixture
def ten_pants_inv():
    inv = Inventory()
    inv.set_stock('Pants', 50.00, 10)
    return inv

@pytest.fixture
def remote_inv_with_pants():
    rsp = MagicMock()
    rsp.status = 200
    rsp.read.return_value = json.dumps({
        'name': 'Pants',
        'price': 50.00,
        'quantity': 10
    })

    client = create_autospec(HTTPConnection)
    client.getresponse.return_value = rsp
    return Inventory(client=client)

@pytest.fixture
def remote_inv_error():
    rsp = MagicMock()
    rsp.status = 404

    client = create_autospec(HTTPConnection)
    client.getresponse.return_value = rsp
    return Inventory(client=client)

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

def test_fetch_remote_stock_success(remote_inv_with_pants):
    remote_inv_with_pants.fetch_remote_stock('Pants')

    assert remote_inv_with_pants.items['Pants']['price'] == 50.00
    assert remote_inv_with_pants.items['Pants']['quantity'] == 10
    assert remote_inv_with_pants.total_stock() == 10

def test_fetch_remote_stock_error(remote_inv_error):
    with pytest.raises(NoSuchItemError):
        remote_inv_error.fetch_remote_stock('Pants')
    
    assert remote_inv_error.total_stock() == 0

def test_fetch_remote_stock_real_server():
    client = HTTPConnection('localhost', 44332)
    inv = Inventory(client=client)
    inv.fetch_remote_stock('Pants')

    assert inv.items['Pants']['price'] == 50.00
    assert inv.items['Pants']['quantity'] == 10
    assert inv.total_stock() == 10
