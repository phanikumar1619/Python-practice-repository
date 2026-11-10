from abc import ABC , abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def withdraw(self):
        pass

class SavingsAccount(BankAccount):
    def withdraw(self):
        print("your savings account was safe")

a = SavingsAccount()
a.withdraw()