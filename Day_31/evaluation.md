# Polynomial Regression – Evaluation

## Evaluation Metrics Used
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

These metrics help measure how well the model predicts unseen data.

## Model Performance
Polynomial Regression (Degree 2) performs better than simple Linear Regression
when the relationship between X and y is non-linear.

- MAE decreases because predictions are closer to actual values
- R² score increases because the curve fits the data better

## Why Polynomial Regression Works Better
Linear Regression fits a straight line, which cannot capture curved patterns.
Polynomial Regression transforms features (x², x³, etc.), allowing the model
to learn non-linear relationships.

## Risk of High-Degree Polynomial
Using a very high polynomial degree can cause overfitting:
- Model fits training data too well
- Performs poorly on new/unseen data

This leads to high variance.

## Interview Question

**Q: Is Polynomial Regression a linear model?**  
**A:** Yes. Polynomial Regression is linear in terms of model parameters
(coefficients), even though the curve looks non-linear.
