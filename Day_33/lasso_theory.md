# Lasso Regression (L1 Regularization)

## What is Lasso Regression?
Lasso Regression is a regularized form of Linear Regression that uses **L1 penalty**.

It adds a penalty proportional to the **absolute values of coefficients**.

---

## Lasso Loss Function
Loss = RSS + λ Σ|w|

Where:
- RSS = Residual Sum of Squares
- λ (lambda) = regularization strength
- w = model coefficients

---

## Key Property of Lasso
- Shrinks coefficients
- Can make some coefficients **exactly zero**
- Performs automatic **feature selection**

---

## Effect on Model
- Removes less important features
- Produces sparse models
- Reduces overfitting

---

## Bias–Variance Impact
- Bias increases
- Variance decreases
- Model becomes simpler and interpretable

---

## When to Use Lasso?
- Dataset has many irrelevant features
- Need feature selection
- Want simpler, interpretable models

