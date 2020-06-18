1.  Our functional code is already pretty compact, so we probably won't be looking
    at it.

    What we illustrate here is refactoring our test code, since it isn't very
    maintainable as-is.

2.  One easy update we can make is to use pytest fixtures. These are used to 
    simplify the setup/teardown of tests.

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

3.  We've added a test, but reduced our code volume by about 25%!