# Ridge Regression (L2 Regularization)

## What is Ridge Regression?
Ridge Regression is a regularized version of Linear Regression that uses **L2 penalty**.

It adds a penalty proportional to the **square of coefficient magnitudes** to the loss function.

---

## Ridge Loss Function
Loss = RSS + λ Σ(w²)

Where:
- RSS = Residual Sum of Squares
- λ (lambda) = regularization strength
- w = model coefficients

---

## Effect of Ridge Regularization
- Shrinks coefficients towards zero
- Never makes coefficients exactly zero
- Reduces overfitting
- Works well when all features are useful

---

## Bias–Variance Impact
- Bias increases slightly
- Variance decreases significantly
- Overall test performance improves

---

## When to Use Ridge?
- Dataset has multicollinearity
- Many features contribute to the output
- Overfitting in Linear Regression
