#!/usr/bin/env python3
"""
module7_knn-regr-scikit.py
Simple k-NN Regression with NumPy + scikit-learn
"""

import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# --- Inputs ---
N = int(input("Enter N (number of points): "))
k = int(input("Enter k (neighbors): "))

if k > N:
    print("Error: k must be <= N")
    exit()

X = []
y = []
for i in range(N):
    x_val = float(input(f"x[{i+1}]: "))
    y_val = float(input(f"y[{i+1}]: "))
    X.append([x_val])   # [[x]] shape for sklearn
    y.append(y_val)

X = np.array(X)
y = np.array(y)

X_query = float(input("Enter query X: "))

# --- k-NN Regression ---
model = KNeighborsRegressor(n_neighbors=k)
model.fit(X, y)
y_pred = model.predict([[X_query]])[0]

# --- Variance of labels ---
variance = np.var(y)

# --- Output ---
print(f"\nPrediction for X = {X_query}: {y_pred:.6f}")
print(f"Variance of labels: {variance:.6f}")
