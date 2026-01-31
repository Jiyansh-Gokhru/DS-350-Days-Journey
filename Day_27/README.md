# Day 27 – Train-Test Split & Baseline Model (Titanic)

## Objective
Build the first machine learning pipeline using the Titanic dataset by:
- Splitting data into training and testing sets
- Training a baseline Logistic Regression model
- Evaluating model performance using multiple metrics

---

## Dataset
Titanic dataset with the following preprocessing:
- Dropped non-numeric columns: Name, Sex, Ticket, Cabin, Embarked
- Handled missing values using median imputation

Target column:
- Survived (0 = Not Survived, 1 = Survived)

---

## Steps Performed

### 1. Train-Test Split
- Split data into 80% training and 20% testing
- Used random_state=42 for reproducibility

### 2. Logistic Regression Model
- Trained a Logistic Regression classifier
- Used as a baseline model for binary classification

### 3. Model Evaluation
- Accuracy Score
- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)

---

## Key Learnings
- Machine learning models require numerical input features
- Missing values must be handled before training
- Accuracy alone is not sufficient to evaluate classification models
- Small datasets can lead to unusual evaluation outputs (e.g., 1×1 confusion matrix)

---

## Conclusion
A complete and correct ML pipeline was built successfully.
This baseline model sets the foundation for advanced models and feature engineering in upcoming days.
