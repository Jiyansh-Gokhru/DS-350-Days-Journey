import pandas as pd
from sklearn.model_selection import train_test_split

# Load cleaned data
df = pd.read_csv("titanic_cleaned.csv")

# Separate features and target
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Train-Test Split (80-20)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Print shapes to verify
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
