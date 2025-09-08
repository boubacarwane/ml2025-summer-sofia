#!/usr/bin/env python3
"""
module9_knn_gridsearchcv.py
Super simple k-NN classifier with GridSearchCV (k = 1..10).
- NumPy for data
- scikit-learn for ML
"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

# --- Read TRAIN data ---
N = int(input("Enter N (training size): "))
X_tr, y_tr = [], []
print("Enter TRAIN pairs (x then y):")
for i in range(N):
    x = float(input(f"x[{i+1}]: "))
    y = int(input(f"y[{i+1}]: "))
    X_tr.append([x])   # shape (N, 1)
    y_tr.append(y)
X_tr = np.array(X_tr, dtype=float)
y_tr = np.array(y_tr, dtype=int)

# --- Read TEST data ---
M = int(input("\nEnter M (test size): "))
X_te, y_te = [], []
print("Enter TEST pairs (x then y):")
for i in range(M):
    x = float(input(f"x[{i+1}]: "))
    y = int(input(f"y[{i+1}]: "))
    X_te.append([x])
    y_te.append(y)
X_te = np.array(X_te, dtype=float)
y_te = np.array(y_te, dtype=int)

# --- Grid search for best k on TRAIN ---
param_grid = {"n_neighbors": list(range(1, 11))}
cv = min(5, len(X_tr)) if len(X_tr) > 1 else 2  # tiny safeguard
grid = GridSearchCV(KNeighborsClassifier(), param_grid, cv=cv, scoring="accuracy", refit=True)
grid.fit(X_tr, y_tr)

best_k = grid.best_params_["n_neighbors"]
best_model = grid.best_estimator_  # already refit on full train

# --- Evaluate on TEST ---
y_pred = best_model.predict(X_te)
acc = accuracy_score(y_te, y_pred)

print(f"\nBest k: {best_k}")
print(f"Test accuracy: {acc:.4f}")
