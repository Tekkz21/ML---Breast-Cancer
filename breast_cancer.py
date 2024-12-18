# -*- coding: utf-8 -*-
"""Breast Cancer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CbxyexrHMIJpxuJgjFAZbP9OAmvKGLyZ
"""

import sklearn
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

bst_cancer = datasets.load_breast_cancer()

print ('Labels:' , bst_cancer.target_names)

print("Features:", bst_cancer.feature_names)

x = bst_cancer.data
y = bst_cancer.target

# Spliting the dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initializing the scaler
scaler = StandardScaler()

# Fitting the scaler on the training data and transform both train and test sets
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

print(x_train [:5], y_train[:5])

model = SVC(kernel='linear', C=1.0, random_state=42)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

# Print metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))