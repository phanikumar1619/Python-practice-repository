from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Engine Started!")
    def stop(self):
        print("Car Engine Stopped!")

class Bike(Vehicle):
    def start(self):
        print("Bike Engine Started!")
    def stop(self):
        print("Bike Engine Stopped!")

class Bus(Vehicle):
    def start(self):
        print("Bus Engine Started!")
    def stop(self):
        print("Bus Engine Stopped!")


print("Select Vehicle:")
print("1. Car")
print("2. Bike")
print("3. Bus")
n = int(input("Enter your choice: "))
if(n == 1):
    a = Car()
    a.start()
    a.stop()
elif(n == 2):
    b = Bike()
    b.start()
    b.stop()
elif(n == 3):
    c = Bus()
    c.start()
    c.stop()