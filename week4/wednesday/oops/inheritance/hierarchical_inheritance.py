class Vehicle:
    def __init__(self , brand):
        self.brand = brand

    def display_brand(self):
        print("Brand Name:" , self.brand)

class Car(Vehicle):

    def __init__(self, brand , car_model):
        super().__init__(brand)
        self.car_model = car_model

    def display_car(self):
        print("car Model:" , self.car_model)

class Bike(Vehicle):

    def __init__(self, brand , bike_model):
        super().__init__(brand)
        self.bike_model = bike_model

    def display_bike(self):
        print("Bike Model:" , self.bike_model)

car = Car("Toyota", "Fortuner")
bike = Bike("Yamaha", "R15")

car.display_brand()
car.display_car()

bike.display_brand()
bike.display_bike()
