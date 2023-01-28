from typing import List


class Configuration():
    def __init__(self, home: str, width: int, height: int, palette: str, order: str, patterns: List):
        self._home = home
        self._width = width
        self._height = height
        self._palette = palette
        self._order = order
        self._patterns = patterns
        self._print = False
        self._write = True

    @property
    def home(self) -> str:
        return self._home

    @property
    def fill(self) -> str:
        return self._fill

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def palette(self) -> str:
        return self._palette

    @property
    def order(self) -> str:
        return self._order

    @property
    def patterns(self) -> str:
        return self._patterns

    @property
    def print(self) -> str:
        return self._print

    @property
    def write(self) -> str:
        return self._write


__all__ = ["Configuration"]
