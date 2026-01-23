import pandas as pd

# Load the CSV
df = pd.read_csv("students.csv")

print("Original DataFrame:")
print(df)

print("\n------------------\n")

# Selecting a single column
print("Names column:")
print(df["Name"])

print("\n------------------\n")

# Selecting multiple columns
print("Name and Marks:")
print(df[["Name", "Marks"]])

print("\n------------------\n")

# Selecting rows using iloc
print("First two rows using iloc:")
print(df.iloc[0:2])

print("\n------------------\n")

# Selecting rows using loc
print("Rows where Marks > 85:")
print(df.loc[df["Marks"] > 85])

print("\n------------------\n")

# Adding a new column
df["Passed"] = df["Marks"] >= 80
print("After adding Passed column:")
print(df)

print("\n------------------\n")

# Dropping a column
df = df.drop("City", axis=1)
print("After dropping City column:")
print(df)
