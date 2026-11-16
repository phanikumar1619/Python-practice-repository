class Product:

    def __init__(self , product_name , __price):
        self.product_name = product_name
        self.__price = __price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self , new_price):
        if(new_price > 0):
            self.__price = new_price
        else:
            print("Invaild Price")

    def display_details(self):
        print("Product Name:" , self.product_name)
        print("Product Price:", self.price)


product = Product("Laptop", 50000)

print(product.price)

product.price = 60000
product.price = -1000
product.price = 0

product.display_details()