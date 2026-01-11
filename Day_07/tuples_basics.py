numbers = (10, 20, 30, 40, 50)
print(numbers)

print(numbers[0])   # first element
print(numbers[-1])  # last element

print(numbers[1:4])

# Tuples cannot be changed
# numbers[0] = 100    #This will give an error

print("Tuples are immutable")

data = (1, 2, 3, 2, 4, 2)

print(data.count(2))   # count occurrences
print(data.index(3))   # index of element

student = ("Jiyansh", 18, "CSE-DS")

name, age, branch = student

print(name)
print(age)
print(branch)
