# Program 1: Print your name
def print_name():
    print("Jiyansh Jain")

print_name()

# Program 2: Add two numbers
def add_numbers(a, b):
    return a + b

print(add_numbers(4, 6))

# Program 3: Even or Odd
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(7))

# Program 4: Maximum of two numbers
def max_two(a, b):
    if a > b:
        return a
    else:
        return b

print(max_two(10, 20))

# Program 5: Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))

# Program 6: Prime number checker
def is_prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

print(is_prime(11))

# Program 7: Simple Interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

print(simple_interest(1000, 5, 2))

# Program 8: Reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

print(reverse_number(1234))

# Program 9: Count digits
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

print(count_digits(56789))

# Program 10: Square & Cube
def square_cube(n):
    return n*n, n*n*n

sq, cb = square_cube(3)
print("Square:", sq, "Cube:", cb)


