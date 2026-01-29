import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("titanic")

# Set style
sns.set(style="whitegrid")

# Age vs Survival (Boxplot)
plt.figure()
sns.boxplot(x="Survived", y="Age", data=df)
plt.title("Age vs Survival")
plt.show()

# Age Distribution by Survival (Histogram)
plt.figure()
sns.histplot(data=df, x="Age", hue="Survived", kde=True)
plt.title("Age Distribution by Survival")
plt.show()

# are vs Survival (Boxplot)
plt.figure()
sns.boxplot(x="Survived", y="Fare", data=df)
plt.title("Fare vs Survival")
plt.show()
