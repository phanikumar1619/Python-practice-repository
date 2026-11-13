class BankAccount():
    def __init__(self , account_holder , balance):
        self.account_holder = account_holder
        self.balance = balance
        self.total_deposit = 0
        self.total_withdraw = 0

    def deposit(self , amount):
        if(amount <= 0):
            print("Please check the amount")
        else:
            self.balance = amount + self.balance
            self.total_deposit = self.total_deposit + amount
            print("Deposited:",self.total_deposit)

    def withdraw(self , amount):
        if(amount > self.balance):
            print("Insufficient Balance")
        elif(amount <= 0):
            print("Plase check the ammount")
        else:
            self.balance = self.balance - amount
            self.total_withdraw = self.total_withdraw + amount
        print("Withdrawn:",self.total_withdraw)

    def display_balance(self):
        print("Account Holder:" , self.account_holder)
        print("Available Balance:" , self.balance)


a1 = BankAccount("Phani", 5000)

a1.deposit(2000)
a1.withdraw(1500)
a1.display_balance()

a2 = BankAccount("kumar", 6000)

a2.deposit(3000)
a2.withdraw(1500)
a2.deposit(1000)
a2.display_balance()