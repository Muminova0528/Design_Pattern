from abc import ABC, abstractmethod


class Copyable(ABC):

    @abstractmethod
    def clone(self):
        pass
