# import os

from ..configuration import Configuration

from .abstract_file_manager import AbstractFileManager
from .abstract_time_manager import AbstractTimeManager


class FileOutputManager(AbstractFileManager):
    def __init__(self, tm: AbstractTimeManager, configuration: Configuration):
        self.tm = tm
        self.configuration = configuration

        # directory = configuration.home + "/files"

        # if not os.path.exists(directory):
        #     return Exception(directory)

    def save(self, output):
        with open(self.configuration.home + "/latest.svg", "w") as out_file:
            out_file.write(output)
        with open(self.configuration.home + "/history/" + self.tm.get_datetime().isoformat(sep="T", timespec="seconds") + ".svg", "w") as out_file:
            out_file.write(output)


__all__ = ["FileOutputManager"]
