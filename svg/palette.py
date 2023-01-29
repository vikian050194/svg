from enum import Enum

from svg.managers.random_manager import AbstractRandomManager


class Order(str, Enum):
    FORWARD = "forward"
    BACKWARD = "backward"
    MONO = "mono"
    RANDOM = "random"
    # SHIFT = "shift"


class Palette():
    def __init__(self, colors: Enum, order: Order, rm: AbstractRandomManager):
        self.colors = [c.value for c in colors]
        self.index = 0
        self.max_index = len(self.colors) - 1 
        self.order = order
        self.rm = rm
        if order == Order.MONO:
            self.index = self.rm.next(0, self.max_index)

    def _get_current_color(self):
        return self.colors[self.index]

    def _get_next_color(self):
        value = self.colors[self.index]
        self.index = 0 if self.index == self.max_index else self.index + 1
        return value

    def _get_previous_color(self):
        value = self.colors[self.index]
        self.index = self.max_index if self.index == 0 else self.index - 1
        return value

    def _get_random_color(self):
        index = self.rm.next(0, self.max_index)
        return self.colors[index]

    def get_color(self):
        if self.order == Order.MONO:
            return self._get_current_color()
        if self.order == Order.FORWARD:
            return self._get_next_color()
        if self.order == Order.BACKWARD:
            return self._get_previous_color()
        if self.order == Order.RANDOM:
            return self._get_random_color()
        raise ValueError(f"{self.order} is invalid value")


__all__ = [
    "Palette",
    "Order"
]
