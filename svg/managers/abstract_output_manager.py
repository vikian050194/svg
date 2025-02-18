import abc


class AbstractOutputManager(abc.ABC):
    @abc.abstractmethod
    def save(self,  output: str) -> None:
        raise NotImplementedError()


__all__ = ["AbstractOutputManager"]
