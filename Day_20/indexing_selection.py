import pandas as pd

# Creating DataFrame
data = {
    "Name": ["Aman", "Riya", "Karan", "Neha", "Rahul"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 88, 92],
    "City": ["Indore", "Bhopal", "Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print("Full DataFrame:\n", df)

# Column selection
print("\nSingle column (Name):\n", df["Name"])
print("\nMultiple columns (Name & Marks):\n", df[["Name", "Marks"]])

# Row selection using iloc
print("\nFirst 3 rows using iloc:\n", df.iloc[0:3])

# Row selection using loc
print("\nRows with index 1 to 3 using loc:\n", df.loc[1:3])

# Row + Column selection
print("\nSpecific rows & columns using loc:\n", df.loc[1:3, ["Name", "Marks"]])
print("\nSpecific rows & columns using iloc:\n", df.iloc[0:3, 0:2])
