class BankAccount():
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if new_balance < 0:
            print("Balance cannot be negative.")
        else:
            self.__balance = new_balance
            print("Balance updated successfully.")

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Initial Balance: {self.__balance}")

a = BankAccount("phani", 50000)
a.display_account_info()
a.set_balance(60000)
a.set_balance(-5000)
print("Final Balance:" , a.get_balance())
print(a._BankAccount__balance)

    