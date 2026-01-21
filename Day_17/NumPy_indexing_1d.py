import numpy as np

# Create 1D array
arr = np.array([10, 20, 30, 40, 50])

# Indexing
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Middle element:", arr[2])

# Slicing
print("First three elements:", arr[0:3])
print("From index 1 to end:", arr[1:])
print("All elements:", arr[:])

# Modify element
arr[1] = 25
print("Modified array:", arr)
