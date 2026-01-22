import numpy as np

marks = np.array([
    [78, 85, 90],
    [88, 92, 79],
    [84, 76, 88]
])

# Column-wise operations
print("Column-wise Sum:", np.sum(marks, axis=0))
print("Column-wise Mean:", np.mean(marks, axis=0))
print("Column-wise Max:", np.max(marks, axis=0))

# Row-wise operations
print("\nRow-wise Sum:", np.sum(marks, axis=1))
print("Row-wise Mean:", np.mean(marks, axis=1))
print("Row-wise Max:", np.max(marks, axis=1))

# Normalization (0 to 1)
normalized = (marks - np.min(marks)) / (np.max(marks) - np.min(marks))
print("\nNormalized Marks:\n", normalized)
