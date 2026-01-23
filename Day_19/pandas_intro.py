import pandas as pd

# Creating a Series
marks = pd.Series([85, 90, 78, 92])
print("Series:")
print(marks)

print("\n------------------\n")

# Creating a DataFrame
data = {
    "Name": ["Aman", "Riya", "Kunal", "Sneha"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)
