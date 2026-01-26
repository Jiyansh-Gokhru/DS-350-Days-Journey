import pandas as pd

# Creating a DataFrame with missing values
data = {
    "Name": ["Aman", "Riya", None, "Kunal"],
    "Age": [20, None, 22, 21],
    "Score": [85, 90, None, 88]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:\n")
print(df)

# Check for missing values (True = missing)
print("\nMissing Values (isnull):\n")
print(df.isnull())

# Check for non-missing values
print("\nNon-Missing Values (notnull):\n")
print(df.notnull())

# Count missing values in each column
print("\nCount of Missing Values per Column:\n")
print(df.isnull().sum())
