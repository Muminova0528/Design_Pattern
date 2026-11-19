from bank_account import BankAccount
from real_bank_account import RealBankAccount


class BankAccountProxy(BankAccount):

    def __init__(self, is_logged_in, balance):
        self.is_logged_in = is_logged_in
        self.real_account = RealBankAccount(balance)

    def withdraw(self, amount: float):
        print("\nPul yechish operatsiyasi boshlandi...")

        if self.is_logged_in:
            print("Avtorizatsiya muvaffaqiyatli!")
            self.real_account.withdraw(amount)
        else:
            print("Xatolik: foydalanuvchi tizimga kirmagan!")
            print("Operatsiya taqiqlanadi.")