# Create a set of numbers
nums = {1, 2, 3, 4, 5}
print(nums)

# Add and remove elements
nums.add(6)
nums.remove(3)
print(nums)

# Union of two sets
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))

# Intersection of two sets
print(a.intersection(b))

# Difference of two sets
print(a.difference(b))

# Remove duplicates from a list using set
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)

print(unique_numbers)

    