from bank_account import BankAccount


class RealBankAccount(BankAccount):

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Xatolik: summa noto'g'ri!")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so'm hisobdan yechildi.")
            print(f"Qolgan balans: {self.balance} so'm")
        else:
            print("Xatolik: hisobda mablag' yetarli emas!")