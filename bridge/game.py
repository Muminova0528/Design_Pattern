from abc import ABC, abstractmethod


class Game(ABC):

    def __init__(self, developer):
        self.developer = developer

    @abstractmethod
    def develop(self):
        pass