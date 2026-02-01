import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# =========================
# Load dataset
# =========================
df = sns.load_dataset("titanic")

df = df[
    [
        "survived",
        "pclass",
        "sex",
        "age",
        "sibsp",
        "parch",
        "fare",
        "embarked",
    ]
].copy()

# =========================
# Data cleaning
# =========================
df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

df["sex"] = df["sex"].map({"male": 0, "female": 1})
df = pd.get_dummies(df, columns=["embarked"], drop_first=True)

# =========================
# Features & target
# =========================
X = df.drop("survived", axis=1)
y = df["survived"]

# =========================
# Train-test split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# Decision Tree Models
# =========================

# Model 1: Default Decision Tree
dt_default = DecisionTreeClassifier(random_state=42)
dt_default.fit(X_train, y_train)
y_pred_default = dt_default.predict(X_test)

print("\n====== Decision Tree (Default) ======")
print("Accuracy:", accuracy_score(y_test, y_pred_default))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_default))
print("Classification Report:\n", classification_report(y_test, y_pred_default))

# Model 2: Controlled Depth Decision Tree
dt_limited = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_limited.fit(X_train, y_train)
y_pred_limited = dt_limited.predict(X_test)

print("\n====== Decision Tree (max_depth=5) ======")
print("Accuracy:", accuracy_score(y_test, y_pred_limited))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_limited))
print("Classification Report:\n", classification_report(y_test, y_pred_limited))
