# Day 26 – Feature Engineering (Titanic Dataset)

## Objective
The objective of this task is to transform raw Titanic dataset features into
machine-learning-ready numerical features using feature engineering techniques.

## Key Tasks
- Handle missing values in key columns
- Create new meaningful features
- Encode categorical variables
- Prepare final feature matrix (X) and target vector (y)

## Feature Engineering Steps
- Filled missing values in:
  - Age (median)
  - Fare (median)
  - Embarked (mode)
- Created new features:
  - FamilySize = SibSp + Parch + 1
  - IsAlone (1 if FamilySize == 1 else 0)
- Dropped non-useful columns:
  - Name, Ticket, Cabin
- Encoded categorical variables:
  - Sex → numerical mapping
  - Embarked → one-hot encoding
  - Pclass → one-hot encoding

## Final Features
The final dataset consists of only numerical features suitable for
machine learning models.

- Feature matrix: `X`
- Target variable: `y` (Survived)

## Output
- Cleaned and engineered feature set ready for:
  - Train-test split
  - Model training
  - Evaluation

## Conclusion
Feature engineering significantly improves the quality of input data by
extracting meaningful patterns and ensuring compatibility with machine
learning algorithms. This step forms the foundation for building effective
predictive models in the next stages.
