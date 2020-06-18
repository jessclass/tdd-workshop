1.  Let's assume we want to add a feature to the Inventory class that allows it to
    retrieve inventory information from a remote server using the name of a
    product. This could be useful if we wanted to centralize inventory data in a 
    server that is accessible to multiple services.

2.  We should add a method fetch_remote_stock to the Inventory object. There are
    a few approaches you could take to do this:

    1.  Give the method a URL to fetch from, and the name of the inventory item
        to retrieve. This will certainly work, but the fact that we supply the
        URL to the object means that the method will have to instantiate a client
        to interact with the server.
    
    2.  Instead, we can use Dependency Injection to provide a mock object to the
        Inventory object which will allow us to control its behavior in test code.
        What's even nicer about this solution is that a server doesn't have to 
        exist at all for us to determine whether our code should work.

3.  Write test cases for fetch_remote_stock. In the interest of time, we will only
    write two cases, though you could certainly write more.

        from unittest.mock import create_autospec, MagicMock
        from http.client import HTTPConnection
        import json

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

        def test_fetch_remote_stock_success(remote_inv_with_pants):
            remote_inv_with_pants.fetch_remote_stock('Pants')

            assert remote_inv_with_pants.items['Pants']['price'] == 50.00
            assert remote_inv_with_pants.items['Pants']['quantity'] == 10
            assert remote_inv_with_pants.total_stock() == 10

        def test_fetch_remote_stock_error(remote_inv_error):
            with pytest.raises(NoSuchItemError):
                remote_inv_error.fetch_remote_stock('Pants')
            
            assert remote_inv_error.total_stock() == 0

4.  These tests should all fail. Now, write the feature!

        # Add this import
        import json

        # Update the constructor
        def __init__(self, limit=100, client=None):
            self._items = {}
            self._limit = limit
            self._client = client
        
        # Add this method
        def fetch_remote_stock(self, name):
            self._client.request('GET', f"/api/inventory/{name}")
            rsp = self._client.getresponse()

            if rsp.status == 200:
                data = json.loads(rsp.read())
                self.set_stock(data['name'], data['price'], data['quantity'])
            else:
                raise NoSuchItemError(f'server did not find {name}')

5.  Tests should all pass!

6.  It's easy to just stop here and say it works, but let's try using a simple HTTP
    server to provide a real response that matches what we expect.

        def test_fetch_remote_stock_real_server():
            client = HTTPConnection('localhost', 44332)
            inv = Inventory(client=client)
            inv.fetch_remote_stock('Pants')

            assert inv.items['Pants']['price'] == 50.00
            assert inv.items['Pants']['quantity'] == 10
            assert inv.total_stock() == 10

7.  All tests are passing, and we have used a real server to prove that our mock
    is a good replacement for our API.
