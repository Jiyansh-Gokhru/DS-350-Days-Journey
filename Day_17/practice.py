import numpy as np

arr = np.array([2, 5, 8, 11, 14, 17, 20])

# 1. Find maximum and minimum
print("Max value:", arr.max())
print("Min value:", arr.min())

# 2. Extract even numbers
even_numbers = arr[arr % 2 == 0]
print("Even numbers:", even_numbers)

# 3. Square elements greater than 10
squared = arr[arr > 10] ** 2
print("Squared values > 10:", squared)

# 4. Replace values less than 10 with 0
arr[arr < 10] = 0
print("Modified array:", arr)

# 5. Slice array (middle values)
print("Middle elements:", arr[2:5])
