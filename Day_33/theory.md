# Regularization – Theory

## 1. Overfitting in Linear Regression
Overfitting happens when a model learns not only the true pattern in the data but also the noise.  
Such a model performs very well on training data but poorly on unseen (test) data.

In linear regression, overfitting usually occurs when:
- The model is too complex
- There are many features
- Coefficients become very large

---

## 2. Why High Model Complexity Causes Overfitting
When model complexity increases:
- The model tries to fit every data point perfectly
- Small changes in input cause large changes in output
- Coefficients grow very large in magnitude

This makes the model unstable and highly sensitive to noise.

---

## 3. What is Regularization?
Regularization is a technique used to **prevent overfitting** by adding a **penalty term** to the loss function.

This penalty discourages large coefficient values, forcing the model to stay simple and more general.

In simple words:
> Regularization tells the model: “Fit the data well, but don’t become too complex.”

---

## 4. Effect of Regularization on Bias and Variance
- Bias: **Slightly increases**
- Variance: **Significantly decreases**

This trade-off helps the model generalize better on unseen data.

---

## 5. Key Intuition
- Regularization shrinks coefficients
- Important features keep reasonable weights
- Less important features get very small weights

As a result, the model becomes more stable and reliable.

---

## 6. Real-Life Analogy
Imagine studying for an exam by memorizing every single question from past papers.  
You may score well on those exact questions, but fail if new questions appear.

Regularization is like focusing on **core concepts instead of memorizing everything**, so you perform well even on new questions.

---

## 7. Summary
- Overfitting = low training error, high test error
- Regularization adds a penalty for large coefficients
- It improves model generalization
- Trades a little bias for much lower variance
