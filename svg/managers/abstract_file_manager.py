import abc


class AbstractFileManager(abc.ABC):
    @abc.abstractmethod
    def save(self) -> None:
        raise NotImplementedError()
    
    # @abc.abstractmethod
    # def get(self, name: str) -> None:
    #     raise NotImplementedError()


__all__ = ["AbstractFileManager"]
