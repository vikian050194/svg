from enum import Enum
from random import randint


class Order(str, Enum):
    STRAIGHT = "straight"
    SHIFT = "shift"
    RANDOM = "random"


class Palette():
    def __init__(self, colors: Enum, order: Order = Order.STRAIGHT):
        self.colors = [c.value for c in colors]
        self.index = 0
        self.max_index = len(self.colors) - 1 
        self.orger = order
        if order == Order.SHIFT:
            self.index = randint(0, self.max_index)

    def get_next_color(self):
        value = self.colors[self.index]
        self.index = 0 if self.index == self.max_index else self.index + 1
        return value

    def get_random_color(self):
        index = randint(0, self.max_index)
        return self.colors[index]

    def get_color(self):
        if self.orger in [Order.STRAIGHT, Order.SHIFT]:
            return self.get_next_color()
        return self.get_random_color()


__all__ = [
    "Palette",
    "Order"
]
