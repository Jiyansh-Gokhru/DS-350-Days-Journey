# Multiple Linear Regression – House Price Prediction

## Problem Statement
Build a Multiple Linear Regression model to predict house prices using multiple features such as income, house age, number of rooms, and location-based attributes.

## Dataset
California Housing Dataset (from sklearn)

Features include:
- MedInc
- HouseAge
- AveRooms
- AveBedrms
- Population
- AveOccup
- Latitude
- Longitude

Target:
- House Price

## Workflow
1. Loaded dataset and performed basic EDA
2. Checked correlations between features
3. Split data into training and testing sets
4. Trained Multiple Linear Regression model
5. Evaluated using MAE, MSE, RMSE, and R² score
6. Interpreted coefficients and model behavior

## Model Evaluation
- MAE: Measures average absolute error
- MSE: Penalizes larger errors
- RMSE: Square root of MSE, interpretable in target units
- R² Score: Explains variance captured by the model

## Key Learnings
- Multiple features improve prediction performance
- Multicollinearity can affect coefficient interpretation
- Model assumes linear relationships

## Interview Questions
**Q1. Difference between Linear and Multiple Linear Regression?**  
Simple Linear Regression uses one feature, while Multiple Linear Regression uses multiple features.

**Q2. What does a coefficient represent?**  
Change in target value when a feature increases by one unit, keeping others constant.

**Q3. When does MLR fail?**  
When assumptions are violated or features are highly correlated.
