import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("titanic")

# Survival Rate by Passenger Class
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="pclass", hue="survived")
plt.title("Survival Count by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.show()

# Age Distribution: Survivors vs Non-Survivors
plt.figure(figsize=(6,4))
sns.histplot(data=df, x="age", hue="survived", bins=30, kde=True)
plt.title("Age Distribution by Survival Status")
plt.show()

# Fare vs Survival (Spread & Outliers)
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="survived", y="fare")
plt.title("Fare Distribution by Survival Status")
plt.show()
