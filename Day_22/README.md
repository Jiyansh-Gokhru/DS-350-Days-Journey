# Day 22 – Pandas Data Cleaning

## Objective
Learn how to clean real-world datasets using Pandas by handling missing values and duplicate data, and understanding the standard data cleaning workflow.

---

##  What is Data Cleaning?
Data cleaning is the process of identifying and correcting:
- Missing values
- Duplicate records
- Incorrect data types
- Inconsistent or invalid data

Clean data is essential for accurate analysis and machine learning models.

---

## Missing Data in Pandas
Missing data occurs when values are not available for certain observations.

### Common representations:
- `NaN`
- `None`
- `NaT`

### Detecting Missing Values:
- `isnull()`
- `notnull()`
- `isnull().sum()`

Missing values can negatively affect calculations and model performance.

---

## Handling Missing Values

### dropna()
Removes rows or columns containing missing values.
- Use when missing data is small or irrelevant.

### fillna()
Replaces missing values with:
- Mean / median (for numerical data)
- Mode or fixed values (for categorical data)

Used when data loss is not acceptable.

---

## Duplicate Data
Duplicate data means repeated rows that can:
- Bias analysis
- Increase dataset size unnecessarily
- Affect model accuracy

### Detecting Duplicates:
- `duplicated()`
- `duplicated().sum()`

### Removing Duplicates:
- `drop_duplicates()`

---

## Standard Data Cleaning Workflow
1. Inspect data (`head()`, `info()`, `describe()`)
2. Handle missing values
3. Detect and remove duplicates
4. Fix incorrect data types
5. Validate cleaned data

---

## Key Learnings
- How to identify and handle missing data
- When to drop vs fill missing values
- How to detect and remove duplicate records
- A practical data cleaning workflow used in real projects

---

## Files Included
- `missing_values.py`
- `handle_missing_values.py`
- `duplicates_and_cleaning.py`

---


