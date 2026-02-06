import numpy as np
from sklearn.linear_model import Lasso

# Sample data
X = np.array([
    [1, 1],
    [1, 2],
    [2, 2],
    [2, 3]
])
y = np.array([1, 1, 2, 2])

# Lasso model
lasso = Lasso(alpha=0.5)
lasso.fit(X, y)

print("Coefficients:", lasso.coef_)
print("Intercept:", lasso.intercept_)
