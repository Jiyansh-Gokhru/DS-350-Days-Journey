import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Load Dataset
df = pd.read_csv("titanic.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Task 1: Feature Engineering

# Age missing indicator
df["age_missing"] = df["age"].isna().astype(int)

# Is child feature
df["is_child"] = df["age"].apply(
    lambda x: 1 if pd.notna(x) and x < 12 else 0
)

# Fare category feature
df["fare_category"] = pd.qcut(
    df["fare"],
    q=3,
    labels=["low", "medium", "high"]
)

# Task 2: Categorical Encoding

# Encode Sex (binary)
df["sex"] = df["sex"].fillna(df["sex"].mode()[0])
df["sex_encoded"] = df["sex"].map({"male": 0, "female": 1})

# One-hot encode Pclass
pclass_dummies = pd.get_dummies(
    df["pclass"],
    prefix="pclass",
    drop_first=True
)

# One-hot encode Fare Category
fare_dummies = pd.get_dummies(
    df["fare_category"],
    prefix="fare",
    drop_first=True
)

# Merge encoded columns
df = pd.concat([df, pclass_dummies, fare_dummies], axis=1)

# Task 3: Feature Scaling

num_features = ["age", "fare"]

# Fill missing age with median (before scaling)
df["age"] = df["age"].fillna(df["age"].median())

# Standard Scaling
scaler_std = StandardScaler()
df[["age_std", "fare_std"]] = scaler_std.fit_transform(
    df[num_features]
)

# Min-Max Scaling
scaler_mm = MinMaxScaler()
df[["age_mm", "fare_mm"]] = scaler_mm.fit_transform(
    df[num_features]
)

# Task 4: Final Dataset (SAFE)

# Select all engineered numeric features automatically
feature_cols = [
    col for col in df.columns
    if col.startswith("pclass_")
    or col.startswith("fare_")
    or col in ["sex_encoded", "is_child", "age_missing", "age_std", "fare_std"]
]

X = df[feature_cols]
y = df["survived"]

print("Code ran successfully.")
print("Features used:")
print(X.columns.tolist())
print("\nFirst 5 rows of X:")
print(X.head())
