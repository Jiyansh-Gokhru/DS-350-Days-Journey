import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

# Generate synthetic data
np.random.seed(42)
X = np.linspace(0, 10, 50).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(0, 0.3, 50)

# Underfitting model (High Bias)
linear_model = LinearRegression()
linear_model.fit(X, y)
y_linear = linear_model.predict(X)

# Overfitting model (High Variance)
poly_model = Pipeline([
    ("poly", PolynomialFeatures(degree=15)),
    ("lr", LinearRegression())
])
poly_model.fit(X, y)
y_poly = poly_model.predict(X)

# Plot
plt.figure()
plt.scatter(X, y)
plt.plot(X, y_linear)
plt.plot(X, y_poly)
plt.xlabel("X")
plt.ylabel("y")
plt.title("Bias–Variance Tradeoff Demo")
plt.show()
