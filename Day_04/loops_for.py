# Day 04 - Python Loops (For Loops)

# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

print("\n")  # Separator for readability

# 2. Print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)

print("\n")

# 3. Print even numbers from 1 to 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

print("\n")

# 4. Print odd numbers from 1 to 100
for i in range(1, 101):
    if i % 2 != 0:
        print(i)
