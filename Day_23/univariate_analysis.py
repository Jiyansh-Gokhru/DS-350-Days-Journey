import pandas as pd

df = pd.read_csv("titanic.csv")

print("---- Numerical Columns ----")

print("\nAge Analysis")
print("Mean:", df["Age"].mean())
print("Median:", df["Age"].median())
print("Min:", df["Age"].min())
print("Max:", df["Age"].max())

print("\nFare Analysis")
print("Mean:", df["Fare"].mean())
print("Median:", df["Fare"].median())
print("Min:", df["Fare"].min())
print("Max:", df["Fare"].max())


print("\n---- Categorical Columns ----")

print("\nSex value counts:")
print(df["Sex"].value_counts())

print("\nPassenger Class value counts:")
print(df["Pclass"].value_counts())

print("\nSurvived value counts:")
print(df["Survived"].value_counts())
