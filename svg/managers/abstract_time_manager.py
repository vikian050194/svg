import abc
from datetime import datetime


class AbstractTimeManager(abc.ABC):
    @abc.abstractmethod
    def get_datetime(self) -> datetime:
        raise NotImplementedError()


__all__ = ["AbstractTimeManager"]
