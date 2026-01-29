import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("titanic")

# Select numerical columns
num_df = df[["survived", "age", "fare", "pclass"]]

# Correlation matrix
corr = num_df.corr()
print(corr)

# Correlation Heatmap
plt.figure()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
