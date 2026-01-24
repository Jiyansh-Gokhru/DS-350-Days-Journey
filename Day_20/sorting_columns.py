import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Rahul"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 88, 92],
    "City": ["Indore", "Bhopal", "Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# Sorting
print("\nSorted by Marks (ascending):\n", df.sort_values(by="Marks"))
print("\nSorted by Marks (descending):\n", df.sort_values(by="Marks", ascending=False))

# Adding new column
df["Passed"] = df["Marks"] >= 80
print("\nDataFrame after adding 'Passed' column:\n", df)

# Adding derived column
df["Marks_Percentage"] = df["Marks"] / 100 * 100
print("\nDataFrame after adding Marks_Percentage:\n", df)
