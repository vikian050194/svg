from enum import Enum
from random import randint


class Palette():
    def __init__(self, colors: Enum):
        self.colors = [c.value for c in colors]
        self.index = 0
        self.max_index = len(self.colors) - 1 
        self.is_random = False

    def get_next_color(self):
        value = self.colors[self.index]
        self.index = 0 if self.index == self.max_index else self.index + 1
        return value

    def get_random_color(self):
        index = randint(0, self.max_index)
        return self.colors[index]

    def get_color(self):
        return self.get_random_color() if self.is_random else self.get_next_color()
