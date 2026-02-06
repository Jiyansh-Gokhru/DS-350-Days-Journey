# Elastic Net Regression

## What is Elastic Net?
Elastic Net is a regularized regression technique that **combines Ridge (L2) and Lasso (L1)** penalties.

It is designed to overcome the limitations of using Ridge or Lasso alone.

---

## Elastic Net Loss Function
Loss = RSS + λ1 Σ|w| + λ2 Σ(w²)

Where:
- λ1 controls Lasso penalty
- λ2 controls Ridge penalty

---

## Why Elastic Net?
- Lasso fails when features are highly correlated
- Ridge cannot perform feature selection

Elastic Net:
- Handles multicollinearity
- Performs feature selection
- Keeps grouped features together

---

## Effect on Coefficients
- Some coefficients become zero
- Others are shrunk smoothly
- More stable than Lasso alone

---

## When to Use Elastic Net?
- Many correlated features
- High-dimensional datasets
- Want both stability and sparsity
