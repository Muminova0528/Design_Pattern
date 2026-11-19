from abc import ABC, abstractmethod


class BankAccount(ABC):

    @abstractmethod
    def withdraw(self, amount: float):
        pass