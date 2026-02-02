# Linear Regression – Interpretation

## What does a coefficient mean?
A coefficient represents the **change in the target variable (y)** for a **one-unit increase in the feature**, 
while keeping all other features constant.

Example:
- If coefficient = 2.5 → y increases by 2.5 units for every 1 unit increase in that feature.

---

## What does the intercept mean?
The intercept is the **predicted value of y when all input features are zero**.

It represents the baseline prediction of the model.

---

## What does R² = 0.82 mean?
- R² (coefficient of determination) measures how well the model explains the variance in the target.
- R² = 0.82 means:
  - **82% of the variance** in y is explained by the model
  - Remaining 18% is due to noise or missing factors

Higher R² → better fit (but not always better model).

---

## When is Linear Regression a bad choice?
Linear Regression performs poorly when:
- Relationship between X and y is **non-linear**
- Dataset contains **many outliers**
- Features are **highly correlated** (multicollinearity)
- Errors are **not normally distributed**
- Variance of errors is not constant (heteroscedasticity)

---

## Why is Linear Regression still important?
- Acts as a **baseline model**
- Extremely **interpretable**
- Helps understand feature relationships
- Frequently asked in interviews
