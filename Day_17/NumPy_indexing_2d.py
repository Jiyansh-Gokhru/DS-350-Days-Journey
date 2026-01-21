import numpy as np

# Create 2D array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Access elements
print("Element at row 0, col 1:", matrix[0, 1])
print("Last element:", matrix[-1, -1])

# Access rows
print("First row:", matrix[0])
print("Last row:", matrix[-1])

# Access columns
print("First column:", matrix[:, 0])
print("Second column:", matrix[:, 1])

# Slicing sub-matrix
print("2x2 sub-matrix:")
print(matrix[0:2, 0:2])
