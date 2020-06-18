class InvalidQuantityError(Exception):
    pass

class NoRoomError(Exception):
    pass

class OutOfStockError(Exception):
    pass

class NoSuchItemError(Exception):
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

    @property
    def limit(self):
        return self._limit

    @property
    def items(self):
        return self._items
