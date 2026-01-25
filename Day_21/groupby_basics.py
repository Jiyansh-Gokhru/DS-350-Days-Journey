import pandas as pd

# Sample DataFrame
data = {
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Employee": ["A", "B", "C", "D", "E", "F"],
    "Salary": [50000, 40000, 55000, 60000, 42000, 58000],
    "Experience": [2, 3, 4, 5, 2, 4]
}

df = pd.DataFrame(data)
print(df)

print("\n--- Grouped by Department ---")
grouped = df.groupby("Department")

# Print groups
for name, group in grouped:
    print(f"\nDepartment: {name}")
    print(group)
