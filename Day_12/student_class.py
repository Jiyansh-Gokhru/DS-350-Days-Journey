class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

    def is_pass(self):
        if self.marks >= 40:
            print("Status: Pass")
        else:
            print("Status: Fail")

s1 = Student("Amit", 101, 78)
s2 = Student("Neha", 102, 35)

s1.display()
s1.is_pass()

print()

s2.display()
s2.is_pass()
