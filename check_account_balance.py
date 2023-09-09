class Balance:
    balance = 0

    def withdraw(self, withdraw_amt):

        try:
            if self.balance - withdraw_amt < 0:
                raise AssertionError
        except AssertionError:
            print(f"Not enough balance in the account. Current balance is {self.balance}")
        else:
            self.balance -= withdraw_amt
            print(f"You have withdrawn {withdraw_amt}$ successfully. "
                  f"Your updated account balance is {self.balance}")

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print(f"You have deposited {dep_amt}$ successfully. "
              f"Your updated account balance is {self.balance}")

    def check_balance(self):
        print(f"your current balance is {self.balance}")


balance = Balance()
balance.check_balance()
balance.deposit(500)
balance.check_balance()
balance.withdraw(700)
