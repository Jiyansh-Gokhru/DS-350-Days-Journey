# Day 28 – Model Improvement & Comparison (Titanic Dataset)

## Objective
The goal of this project was to move beyond a single baseline model and
compare multiple machine learning algorithms on the Titanic survival dataset.
This helps understand how different models behave on the same data and why
accuracy alone is not sufficient to choose the best model.

---

## Dataset
- Source: Seaborn built-in Titanic dataset
- Target variable: `survived`
- Features used:
  - pclass
  - sex
  - age
  - sibsp
  - parch
  - fare
  - embarked (one-hot encoded)

Missing values were handled using:
- Median imputation for `age`
- Mode imputation for `embarked`

---

## Models Trained

### 1. Logistic Regression (Baseline)
- Used as a simple and interpretable baseline model
- Helps understand linear decision boundaries

### 2. K-Nearest Neighbors (KNN)
- Trained with multiple values of `k` (3, 5, 7)
- Best performance observed at `k = 5`
- Sensitive to feature scaling and noise

### 3. Decision Tree
- Default Decision Tree showed signs of overfitting
- Controlled model with `max_depth = 5` generalized better

---

## Evaluation Metrics
Models were evaluated using:
- Accuracy
- Precision
- R
