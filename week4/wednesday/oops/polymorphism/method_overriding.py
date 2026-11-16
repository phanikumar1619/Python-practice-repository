class Payment:

    def __init__(self , amount):
        self.amount = amount

    def process_payment(self):
        print("Processing general payment")

class UPIPayment(Payment):

    def __init__(self, amount):
        super().__init__(amount)

    def process_payment(self):
        super().process_payment()
        print("Processing UPI payment of : " , self.amount)

class CardPayment(Payment):

    def __init__(self, amount):
        super().__init__(amount)

    def process_payment(self):
        super().process_payment()
        print("Processing Card payment of : ", self.amount)


upi = UPIPayment(500)
card = CardPayment(1000)

upi.process_payment()
card.process_payment()