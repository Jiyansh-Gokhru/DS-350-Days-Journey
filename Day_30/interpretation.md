# Interpretation of Multiple Linear Regression

## What do coefficients mean?
Each coefficient represents the change in the target variable when the corresponding feature increases by 1 unit, **keeping all other features constant**.

## Intercept Interpretation
The intercept is the predicted value of the target when all input features are zero.
In real-world datasets, this may not always be practically meaningful.

## Feature Impact
Features with larger absolute coefficient values have a stronger impact on the target variable.

Positive coefficient:
- Increase in feature → increase in target

Negative coefficient:
- Increase in feature → decrease in target

## Why Multiple Linear Regression?
- Uses multiple factors to make predictions
- More realistic than Simple Linear Regression
- Captures combined effects of features

## Multicollinearity Issue
When independent variables are highly correlated with each other, coefficient values become unstable and hard to interpret.

## Limitations of MLR
- Assumes linear relationship
- Sensitive to outliers
- Poor performance if assumptions are violated

## Interview Answer Example
Multiple Linear Regression predicts a continuous value using multiple features. Each coefficient shows how much the target changes when one feature changes, assuming others stay constant.
