class Payment:

    def __init__(self , amount):
        self.amount = amount

    def pay(self):
        print("Processing general payment")

class UPIPayment(Payment):

    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print("UPI Payment:", self.amount)

class CardPayment(Payment):

    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print("Card Payment:" , self.amount)

class CashPayment(Payment):

    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print("Cash Payment:" , self.amount)


payments = [
    UPIPayment(500),
    CardPayment(1000),
    CashPayment(200)
]

total = 0

for payment in payments:
    payment.pay()
    total += payment.amount

print("Total Payment:", total)