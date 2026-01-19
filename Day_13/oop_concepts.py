class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)   # calling parent constructor
        self.roll_no = roll_no
        self.course = course

    def display_info(self):   # method overriding (polymorphism)
        super().display_info()
        print(f"Roll No: {self.roll_no}")
        print(f"Course: {self.course}")


# object creation
s1 = Student("Jiyansh", 18, 101, "Data Science")
s1.display_info()
