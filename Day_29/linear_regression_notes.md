# Linear Regression – Core Notes

## What is Linear Regression?
Linear Regression is a **supervised learning algorithm** used to model the relationship between:
- **Independent variable(s)** (X)
- **Dependent variable** (y)

It assumes a **linear relationship** between X and y.

---

## Mathematical Equation
### Simple Linear Regression
\[
y = mx + c
\]
Where:
- **m** = slope (coefficient)
- **c** = intercept

### Multiple Linear Regression
\[
y = b_0 + b_1x_1 + b_2x_2 + ... + b_nx_n
\]

---

## Goal of Linear Regression
- Find the **best fit line** that minimizes prediction error
- Achieved by minimizing the **cost function**

---

## Cost Function (Mean Squared Error – MSE)
\[
J = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
\]

- Penalizes larger errors more
- Differentiable → easy to optimize

---

## Key Assumptions of Linear Regression
1. **Linearity** – relationship between X and y is linear
2. **Independence** – observations are independent
3. **Homoscedasticity** – constant variance of errors
4. **Normality of Errors** – residuals follow normal distribution
5. **No Multicollinearity** – features should not be highly correlated

---

## Simple vs Multiple Linear Regression
| Simple | Multiple |
|------|---------|
| One independent variable | Multiple independent variables |
| Easier to interpret | More realistic |
| Less powerful | More predictive |

---

## Evaluation Metrics Used
- **MAE (Mean Absolute Error)**
- **MSE (Mean Squared Error)**
- **RMSE (Root Mean Squared Error)**
- **R² Score**

---

## Advantages
- Easy to understand & implement
- Fast to train
- Highly interpretable
- Good baseline model

---

## Limitations
- Assumes linearity
- Sensitive to outliers
- Poor performance on complex relationships
- Not suitable for non-linear data

---

## When to Use Linear Regression
- Relationship is approximately linear
- Dataset is not extremely noisy
- Interpretability is important
