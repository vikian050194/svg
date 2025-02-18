from ..configuration import Configuration

from .abstract_output_manager import AbstractOutputManager


class TerminalOutputManager(AbstractOutputManager):
    def __init__(self, configuration: Configuration):
        self.configuration = configuration

    def save(self, output):
        print(output)


__all__ = ["TerminalOutputManager"]
