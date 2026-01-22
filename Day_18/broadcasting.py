import numpy as np

# 1. Scalar with 1D array
arr1 = np.array([1, 2, 3, 4, 5])
result1 = arr1 + 10
print("Scalar + 1D Array:", result1)

# 2. 1D array with 2D array
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr3 = np.array([10, 20, 30])
result2 = arr2 + arr3
print("\n1D + 2D Array:\n", result2)

# 3. Column vector with matrix
col_vector = np.array([[1], [2]])
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

result3 = matrix * col_vector
print("\nColumn Vector * Matrix:\n", result3)
