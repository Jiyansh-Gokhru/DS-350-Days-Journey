import pandas as pd

# Creating a DataFrame with duplicate rows
data = {
    "ID": [1, 2, 2, 3, 4, 4],
    "Name": ["Aman", "Riya", "Riya", "Kunal", "Neha", "Neha"],
    "Age": [20, 21, 21, 22, 23, 23],
    "Score": [85, 90, 90, 88, 92, 92]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n")
print(df)

# ---------------- DUPLICATE CHECK ----------------

# Check duplicate rows
print("\nDuplicate Rows (True means duplicate):\n")
print(df.duplicated())

# Count total duplicate rows
print("\nTotal number of duplicate rows:")
print(df.duplicated().sum())

# ---------------- REMOVE DUPLICATES ----------------

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

print("\nDataFrame after removing duplicates:\n")
print(df_no_duplicates)

# ---------------- BASIC DATA CLEANING WORKFLOW ----------------
# 1. Inspect data using head(), info(), describe()
# 2. Handle missing values using dropna() or fillna()
# 3. Detect and remove duplicate rows
# 4. Fix incorrect data types (astype)
# 5. Validate cleaned data
