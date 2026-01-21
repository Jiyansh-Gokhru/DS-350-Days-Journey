import numpy as np

# Create arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

# Element-wise operations
print("Addition:", arr1 + arr2)
print("Subtraction:", arr2 - arr1)
print("Multiplication:", arr1 * arr2)
print("Division:", arr2 / arr1)

# Array with scalar
print("Array * 2:", arr1 * 2)
print("Array + 5:", arr1 + 5)

# Comparison operations
print("arr1 > 3:", arr1 > 3)
print("arr2 == 30:", arr2 == 30)

# Boolean masking
print("Elements of arr1 > 3:", arr1[arr1 > 3])
print("Elements of arr2 < 40:", arr2[arr2 < 40])
