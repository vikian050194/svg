import os
import abc

from .time_manager import AbstractTimeManager
from ..configuration import Configuration


class AbstractOutputManager(abc.ABC):
    @abc.abstractmethod
    def save(self,  output: str) -> None:
        raise NotImplementedError()


class FileOutputManager(AbstractOutputManager):
    def __init__(self, tm: AbstractTimeManager, configuration: Configuration):
        self.tm = tm
        self.configuration = configuration

        directory = configuration.home + "/history"

        if not os.path.exists(directory):
            os.makedirs(directory)

    def save(self, output):
        with open(self.configuration.home + "/latest.svg", "w") as out_file:
            out_file.write(output)
        with open(self.configuration.home + "/history/" + self.tm.get_datetime().isoformat(sep="T", timespec="seconds") + ".svg", "w") as out_file:
            out_file.write(output)


class TerminalOutputManager(AbstractOutputManager):
    def __init__(self, configuration: Configuration):
        self.configuration = configuration

    def save(self, output):
        print(output)


__all__ = [
    "FileOutputManager",
    "TerminalOutputManager"
]
