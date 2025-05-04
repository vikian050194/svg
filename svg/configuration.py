from typing import List


# TODO use dataclass
class Configuration():
    def __init__(self, home: str, width: int, height: int, palettes: List[str], order: str, patterns: List, print_result: bool = False, write_results: bool = True):
        self._home = home
        self._width = width
        self._height = height
        self._palettes = palettes
        self._order = order
        self._patterns = patterns
        self._print = print_result
        self._write = write_results

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
    def palettes(self) -> List[str]:
        return self._palettes

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
