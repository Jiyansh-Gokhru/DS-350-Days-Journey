import numpy as np
from sklearn.linear_model import ElasticNet

# Sample data
X = np.array([
    [1, 1],
    [1, 2],
    [2, 2],
    [2, 3]
])
y = np.array([1, 1, 2, 2])

# Elastic Net model
enet = ElasticNet(alpha=0.5, l1_ratio=0.5)
enet.fit(X, y)

print("Coefficients:", enet.coef_)
print("Intercept:", enet.intercept_)

