from abc import ABC, abstractmethod
import math

class Form(ABC):
    @abstractmethod
    def field_hisobla(self):
        pass

    @abstractmethod
    def perimeter_hisobla(self):
        pass

class Rectangle(Form):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def field_hisobla(self):
        return self.length * self.width

    def perimeter_hisobla(self):
        return 2 * (self.length + self.width)

class Circle(Form):
    def __init__(self, radius):
        self.radius = radius

    def field_hisobla(self):
        return math.pi * (self.radius ** 2)

    def perimeter_hisobla(self):
        return 2 * math.pi * self.radius

class Triangle(Form):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def field_hisobla(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter_hisobla(self):
        return self.side1 + self.side2 + self.side3


rectangle = Rectangle(5, 10)
circle = Circle(7)
triangle = Triangle(3, 4, 5)

print(rectangle.field_hisobla())
print(rectangle.perimeter_hisobla())

print(circle.field_hisobla())
print(circle.perimeter_hisobla())

print(triangle.field_hisobla())
print(triangle.perimeter_hisobla())
