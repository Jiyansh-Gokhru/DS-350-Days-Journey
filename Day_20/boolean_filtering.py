import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Rahul"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 88, 92],
    "City": ["Indore", "Bhopal", "Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# Single condition
print("\nStudents with Marks > 85:\n", df[df["Marks"] > 85])

# Multiple conditions (AND)
print("\nStudents with Age > 20 AND Marks > 85:\n",
      df[(df["Age"] > 20) & (df["Marks"] > 85)])

# Multiple conditions (OR)
print("\nStudents from Indore OR Pune:\n",
      df[(df["City"] == "Indore") | (df["City"] == "Pune")])

# Using isin()
print("\nStudents from selected cities:\n",
      df[df["City"].isin(["Delhi", "Mumbai"])])
