import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Employee": ["A", "B", "C", "D", "E", "F"],
    "Salary": [50000, 40000, 55000, 60000, 42000, 58000],
    "Experience": [2, 3, 4, 5, 2, 4]
}

df = pd.DataFrame(data)

grouped = df.groupby("Department")

# Basic aggregations
print("\nMean Salary by Department")
print(grouped["Salary"].mean())

print("\nTotal Salary by Department")
print(grouped["Salary"].sum())

print("\nEmployee Count by Department")
print(grouped["Employee"].count())

print("\nMultiple Aggregations using agg()")

result = grouped.agg({
    "Salary": ["mean", "max", "min"],
    "Experience": "mean"
})

print(result)
