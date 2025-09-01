import numpy as np
from sklearn.metrics import precision_score, recall_score

# Ask for N
N = int(input("Enter N (positive integer): "))

# Read ground truth (X) and predictions (Y)
X = np.zeros(N, dtype=int)
Y = np.zeros(N, dtype=int)

for i in range(N):
    X[i] = int(input(f"Point {i+1} - x (0/1): "))
    Y[i] = int(input(f"Point {i+1} - y (0/1): "))

# Compute Precision and Recall
precision = precision_score(X, Y, zero_division=0)
recall = recall_score(X, Y, zero_division=0)

print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
