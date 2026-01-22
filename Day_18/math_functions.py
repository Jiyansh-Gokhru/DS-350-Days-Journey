import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr)

# Basic aggregations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))

# Min & Max
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))

# Mathematical operations
print("Square Root:", np.sqrt(arr))
print("Log:", np.log(arr))
print("Exponential:", np.exp(arr))

# Rounding functions
arr2 = np.array([1.2, 2.5, 3.7, 4.1])
print("Round:", np.round(arr2))
print("Floor:", np.floor(arr2))
print("Ceil:", np.ceil(arr2))
