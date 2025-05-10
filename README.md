# 📩 Spam-Detection-Classifier

A machine learning-based web application that detects whether a message (SMS or email) is Spam or Ham using a Naive Bayes classifier. This project is built with Python, scikit-learn, and Streamlit, and is trained on a custom-labeled dataset combining the UCI SMS Spam Collection and hand-crafted messages.

Check out my application: [click here](https://spam-ham-detection.streamlit.app/)

## 🧠 Model Overview

- **Algorithm Used**: Naive Bayes (MultinomialNB)
- **Model Type**: Supervised Learning (Binary Classification)
- **Dataset Size**: 6,731 labeled messages  
  - **Sources**:
    - [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)
    - Custom-generated spam and ham messages
- **Labels**: `spam` or `ham`

---

## 🛠️ Tech Stack

- **Language**: Python 🐍
- **Libraries**:
  - `pandas` for data manipulation
  - `scikit-learn` for machine learning
  - `Streamlit` for UI/web app deployment
- **Vectorization**: CountVectorizer
- **Deployment**: Streamlit app

---

## 📊 Performance Metrics

| Metric     | Score    |
|------------|----------|
| Accuracy   | 99.33%   |
| Precision  | 94.88%   |
| Recall     | 98.93%   |
| F1 Score   | 96.86%   |

> These results indicate a highly effective spam detection model, with strong recall to minimize false negatives (i.e., spam messages missed by the classifier).

Feel free to contribute, modify, or use the code according to the terms of the license.
---
