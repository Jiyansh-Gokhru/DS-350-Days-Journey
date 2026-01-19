from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, rate_per_hour):
        super().__init__(name, emp_id)
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        return self.hours_worked * self.rate_per_hour


# polymorphism in action
employees = [
    FullTimeEmployee("Aman", 101, 50000),
    PartTimeEmployee("Riya", 102, 120, 400)
]

for emp in employees:
    print(f"Employee: {emp.name} | Salary: {emp.calculate_salary()}")
