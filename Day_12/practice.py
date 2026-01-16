class BankAccount():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} has been deposited! \n Acc. balace is {self.balance}")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"{amount} has been withdrawn! \n Acc. balace is {self.balance}")
        else:
            print("Insufficient balance")
    def show_balance(self):
        print(f"Your current balance is {self.balance}")

person1=BankAccount("Mohit",82000)
person1.deposit(3000)
person1.withdraw(10000)
person1.show_balance()