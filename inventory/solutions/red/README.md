# Lecture
1.  Add initial tests for creating Inventory and setting stock:

        from inventory import Inventory, NoRoomError, InvalidQuantityError

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

2.  Verify that these tests fail

        pytest

3.  Implement Inventory class to fix tests

        class InvalidQuantityError(Exception):
            pass

        class NoRoomError(Exception):
            pass

        class Inventory:
            def __init__(self, limit=100):
                self._items = {}
                self._limit = limit
            
            def set_stock(self, name, price, quantity):
                if quantity < 0:
                    raise InvalidQuantityError(f'invalid stock value: {quantity}')
                elif self.total_stock() + quantity > self._limit:
                    raise NoRoomError(f'adding {quantity} would exceed limit of {self._limit}')
                else:
                    self._items[name] = {
                        'price': price,
                        'quantity': quantity
                    }

            def total_stock(self):
                return sum(v['quantity'] for _, v in self._items.items())

            @property
            def limit(self):
                return self._limit

            @property
            def items(self):
                return self._items

4.  Run pytest and check that the addition of stock is working

        pytest

# Student Activity
1.  Implement remove_stock() using TDD!

# Student Activity Solution
1.  Think about what test cases you need.
2.  Write tests assuming that the feature exists.

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

3.  Write functional code to make those tests pass.

        class OutOfStockError(Exception):
            pass

        class NoSuchItemError(Exception):
            pass

        def remove_stock(self, name, quantity):
            if quantity < 0:
                raise InvalidQuantityError(f'invalid quantity: {quantity}')
            elif name not in self._items:
                raise NoSuchItemError(f'we do not sell: {name}')
            elif self._items[name]['quantity'] - quantity < 0:
                raise OutOfStockError(f'insufficient stock to buy {quantity} of {name}')
            else:
                self._items[name]['quantity'] -= quantity

4.  Great! We should be at green!