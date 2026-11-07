
from abc import ABC, abstractmethod


class IConnection(ABC):

    @abstractmethod
    def get_session(self):
        pass