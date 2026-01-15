# Program 1: Division with error handling
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Please enter valid integers")

finally:
    print("Program finished")

# Program 2: Safe integer input
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)

except ValueError:
    print("Invalid input! Integer required.")

# Program 3: Simple calculator (with try-except)
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    op = input("Enter operation (+ - * /): ")

    if op == "+":
        print("Result:", x + y)
    elif op == "-":
        print("Result:", x - y)
    elif op == "*":
        print("Result:", x * y)
    elif op == "/":
        print("Result:", x / y)
    else:
        print("Invalid operator")

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter numbers only")
