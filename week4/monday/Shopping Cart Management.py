class ShoppingCart():

    store_name = "Amazon"

    def __init__(self , customer_name):
        self.customer_name = customer_name
        self.cart_total = 0

    def add_item(self , price):
        self.cart_total += price

    def display_cart(self):
        print("Customer Name:",self.customer_name)
        print("Store Name:",self.store_name)
        print("Cart Total:",self.cart_total)
        print("\n")

    @classmethod
    def change_store(cls , new_name):
        cls.store_name = new_name

    @staticmethod
    def apply_discount(price, discount):
        final = price - ((price * discount)/ 100)
        return final


c1 = ShoppingCart("Phani")
c1.add_item(1000)
c1.add_item(2000)

c2 = ShoppingCart("Rahul")
c2.add_item(1500)
c2.add_item(500)

c1.display_cart()
c2.display_cart()

ShoppingCart.change_store("Flipkart")

c1.display_cart()
c2.display_cart()

discounted_price = ShoppingCart.apply_discount(2000, 10)
print("Discounted Price:", discounted_price)