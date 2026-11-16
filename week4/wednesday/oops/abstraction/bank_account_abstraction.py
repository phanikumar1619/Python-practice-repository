from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self , account_holder , __balance):
        self.account_holder = account_holder
        self.__balance = __balance

    @property
    def balance(self):
        return self.__balance


    def _deposit_amount(self, amount):
        self.__balance += amount

    def _withdraw_amount(self, amount):
        self.__balance -= amount

    
    @abstractmethod
    def deposit(self , amount):
        pass

    @abstractmethod
    def withdraw(self , amount):
        pass

class SavingsAccount(BankAccount):

    def __init__(self, account_holder, __balance):
        super().__init__(account_holder, __balance)

    def deposit(self, amount):
        if(amount > 0):
            self._deposit_amount(amount)
        else:
            print("Invalid deposit money")

    def withdraw(self, amount):
        if(amount > 0 and amount <= self.balance):
            self._withdraw_amount(amount)
        else:
            print("Invalid withdraw money")

account = SavingsAccount("Phani", 5000)

account.deposit(2000)
account.withdraw(1000)
account.withdraw(10000)

print("Final Balance:", account.balance)