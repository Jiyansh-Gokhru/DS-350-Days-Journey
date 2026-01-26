import pandas as pd

# Creating a DataFrame with missing values
data = {
    "Name": ["Aman", "Riya", None, "Kunal"],
    "Age": [20, None, 22, 21],
    "Score": [85, 90, None, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n")
print(df)

# ---------------- DROPNA ----------------

# Drop rows with any missing values
print("\nDataFrame after dropping rows with missing values:\n")
print(df.dropna())

# Drop columns with any missing values
print("\nDataFrame after dropping columns with missing values:\n")
print(df.dropna(axis=1))

# ---------------- FILLNA ----------------

# Fill missing Age with mean age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Name with 'Unknown'
df["Name"] = df["Name"].fillna("Unknown")

# Fill missing Score with 0
df["Score"] = df["Score"].fillna(0)

print("\nDataFrame after filling missing values:\n")
print(df)
