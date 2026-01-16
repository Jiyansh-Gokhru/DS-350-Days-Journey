class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = Person("Rahul", 20)
p2 = Person("Anita", 22)

p1.greet()
p2.greet()
