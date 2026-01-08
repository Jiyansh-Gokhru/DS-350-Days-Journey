# Day 04 - Python Loops (While Loops)

# 1. Sum of first n natural numbers
n = int(input("Enter n: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum:", total)
print("\n")

# 2. Multiplication table of a number
n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1
print("\n")

# 3. Factorial of a number
n = int(input("Enter number: "))
i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:", fact)
print("\n")

# 4. Count digits in a number
n = int(input("Enter number: "))
count = 0
while n > 0:
    n = n // 10
    count += 1
print("Number of digits:", count)
print("\n")

# 5. Reverse a number
n = int(input("Enter number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reversed number:", rev)
print("\n")

# 6. Simple password check
password = "python123"
while True:
    check = input("Enter password: ")
    if password == check:
        print("Access granted")
        break
    else:
        print("Wrong password, try again")
