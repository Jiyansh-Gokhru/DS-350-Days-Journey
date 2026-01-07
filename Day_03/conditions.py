# Program 1: Positive / Negative / Zero

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Program 2: Largest of two numbers

a = int(input("Enter number_a: "))
b = int(input("Enter number_b: "))

if a==b:
    print(f"{a} is equal to {b}")

elif a>b:
    print(f"{a} is Larger than {b}")

else:
    print(f"{b} is Larger than {a}")

# Program 3: Largest of 3 numbers

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
c = int(input("Enter number C: "))

if a >= b and a >= c:
    if a == b and a == c:
        print("All three numbers are equal")
    else:
        print(f"{a} is the largest number")

elif b >= a and b >= c:
    print(f"{b} is the largest number")

else:
    print(f"{c} is the largest number")

# Program 4: Leap Year Checker

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")

# Program 5: Grading system

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Program 6: Divisible by 3 and 5
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")

# Program 7: Vowel or Consonant
ch = input("Enter a character: ").lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# Program 8: Simple Login System
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")


