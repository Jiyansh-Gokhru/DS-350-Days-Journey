# Create a tuple of 5 numbers
nums = (5, 10, 15, 20, 25)
print(nums)

# Access first and last element
print(nums[0])
print(nums[-1])

# Count occurrence of an element
print(nums.count(10))

# Find index of an element
print(nums.index(15))

# Tuple unpacking
student = ("Jiyansh", 18, "Data Science")
name, age, course = student

print(name)
print(age)
print(course)

# Check if an element exists in tuple
if 20 in nums:
    print("20 is present")
else:
    print("20 is not present")

