from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def movement(self):
        pass

class Car(Transport):
    def movement(self):
        print("The car is driven by wheels.")

class Bike(Transport):
    def movement(self):
        print("The bike is driven by pedals.")

class Plane(Transport):
    def movement(self):
        print("The plane is flown and flied.")

car = Car()
bike = Bike()
plane = Plane()

car.movement()
bike.movement()
plane.movement()  
