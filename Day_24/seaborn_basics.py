import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("titanic")

# Count Plot: Survival by Sex
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="sex", hue="survived")
plt.title("Survival Count by Gender")
plt.show()

# Histogram: Age distribution
plt.figure(figsize=(6,4))
sns.histplot(df["age"], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()

# Box Plot: Age vs Survival
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="survived", y="age")
plt.title("Age vs Survival")
plt.show()

# Heatmap: Correlation
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
