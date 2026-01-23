import pandas as pd

# Load CSV file
df = pd.read_csv("students.csv")

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nShape of DataFrame:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataFrame info:")
print(df.info())

print("\nStatistical summary:")
print(df.describe())
