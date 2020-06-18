import json

class InvalidQuantityError(Exception):
    pass

class NoRoomError(Exception):
    pass

class OutOfStockError(Exception):
    pass

class NoSuchItemError(Exception):
    pass

class Inventory:
    def __init__(self, limit=100, client=None):
        self._items = {}
        self._limit = limit
        self._client = client
    
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

    def remove_stock(self, name, quantity):
        if quantity < 0:
            raise InvalidQuantityError(f'invalid quantity: {quantity}')
        elif name not in self._items:
            raise NoSuchItemError(f'we do not sell: {name}')
        elif self._items[name]['quantity'] - quantity < 0:
            raise OutOfStockError(f'insufficient stock to buy {quantity} of {name}')
        else:
            self._items[name]['quantity'] -= quantity

    def total_stock(self):
        return sum(v['quantity'] for _, v in self._items.items())

    def fetch_remote_stock(self, name):
        self._client.request('GET', f"/api/inventory/{name}")
        rsp = self._client.getresponse()

        if rsp.status == 200:
            data = json.loads(rsp.read())
            self.set_stock(data['name'], data['price'], data['quantity'])
        else:
            raise NoSuchItemError(f'server did not find {name}')

    @property
    def limit(self):
        return self._limit

    @property
    def items(self):
        return self._items
