import pandas as pd

df = pd.read_csv("titanic.csv")

print(df.head())
print("\nShape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nDescribe:")
print(df.describe())
