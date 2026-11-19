from bank_account_proxy import BankAccountProxy


class BankApp:

    def run(self):
        print("===== BANK TIZIMI =====")

        print("\n1. FOYDALANUVCHI: LOGIN QILGAN")

        account1 = BankAccountProxy(
            is_logged_in=True,
            balance=1000000
        )

        account1.withdraw(200000)

        print("\n2. FOYDALANUVCHI: LOGIN QILMAGAN")

        account2 = BankAccountProxy(
            is_logged_in=False,
            balance=1000000
        )

        account2.withdraw(300000)


app = BankApp()
app.run()