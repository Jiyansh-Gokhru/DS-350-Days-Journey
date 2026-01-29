import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("titanic")

# Survival vs Sex
plt.figure()
sns.countplot(x="sex", hue="survived", data=df)
plt.title("Survival Count by Sex")
plt.show()

# Survival vs Passenger Class
plt.figure()
sns.countplot(x="pclass", hue="survived", data=df)
plt.title("Survival Count by Passenger Class")
plt.show()

# Survival vs Embarked
plt.figure()
sns.countplot(x="embarked", hue="survived", data=df)
plt.title("Survival Count by Embarkation Port")
plt.show()
