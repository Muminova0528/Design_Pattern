from abc import ABC, abstractmethod


class FileSystem(ABC):

    @abstractmethod
    def show(self) -> None:
        pass