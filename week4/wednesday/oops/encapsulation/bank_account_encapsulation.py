class BankAccount:

    def __init__(self , account_holder , __account_number , __initial_balance):
        self.account_holder = account_holder
        self.__account_number = __account_number
        self.__initial_balance = __initial_balance

    @property
    def accont_number(self):
        return self.__account_number

    @property
    def initial_balance(self):
        return self.__initial_balance

    @initial_balance.setter
    def initial_balance(self , balance):
        if(balance >= 0):
            print("Uptaded successfully")
            self.__initial_balance = balance
        else:
            print("Invalid Balance")

    def deposit(self , amount):
        if(amount > 0):
            print("Deposit Successful:" , amount)
            self.__initial_balance += amount
        else:
            print("Invalid Deposit Amount")

    def withdraw(self , amount):
        if(amount > 0 and amount <= self.__initial_balance):
            print("Withdrawal Successful:" , amount)
            self.__initial_balance -= amount
        else:
            print("Insufficient Balance")

    def display_account_details(self):
        print("Account Holder:" , self.account_holder)
        print("Account Number:" , self.accont_number)
        print("Current Balance:" , self.initial_balance)



account = BankAccount("Phani", 123456, 50000)

account.deposit(10000)
account.withdraw(15000)
account.withdraw(60000)
account.deposit(-500)
account.initial_balance = -1000

account.display_account_details()