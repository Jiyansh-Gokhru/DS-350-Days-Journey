import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Employee": ["A", "B", "C", "D", "E", "F"],
    "Salary": [50000, 40000, 55000, 60000, 42000, 58000],
    "Experience": [2, 3, 4, 5, 2, 4]
}

df = pd.DataFrame(data)
grouped = df.groupby("Department")

# apply(): works on entire group
print("\nApply example (max salary row per department)")
apply_result = grouped.apply(lambda x: x[x["Salary"] == x["Salary"].max()])
print(apply_result)

# transform(): returns same shape as original data
df["Salary_Zscore"] = grouped["Salary"].transform(
    lambda x: (x - x.mean()) / x.std()
)

print("\nDataFrame with transformed column:")
print(df)
