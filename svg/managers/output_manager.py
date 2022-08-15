import os
import abc
from datetime import datetime

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

        self.folder = "output"
        # wd = "/home/kirill/git/personal/svg/"
        # folder = wd + folder

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)


    def save(self, output):
        with open("output.svg", "w") as out_file:
            out_file.write(output)
        with open(self.folder + "/" + self.tm.get_datetime().isoformat(sep="T", timespec="seconds") + ".svg", "w") as out_file:
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
