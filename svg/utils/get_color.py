from random import randint
from .color import Color

colors = [c.value for c in Color]
color_index = 0
color_max = len(colors) - 1 

def get_color():
    global color_index
    value = colors[color_index]
    color_index = 0 if color_index == color_max else color_index + 1

    return value

def get_random_color():
    index = randint(0, color_max)
    return colors[index]