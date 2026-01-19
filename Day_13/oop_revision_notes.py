# Class & Object
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)

p1 = Person("Jiyansh")
p1.greet()

# Inheritance
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def show(self):
        print(self.name, self.roll)

s1 = Student("Jiyansh", 101)
s1.show()

# Encapsulation
class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

# Polymorphism
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

for animal in (Cat(), Dog()):
    animal.sound()

# Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area of square")

sq = Square()
sq.area()
