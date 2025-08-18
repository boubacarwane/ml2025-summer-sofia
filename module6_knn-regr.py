#!/usr/bin/env python3


from __future__ import annotations
import sys
import numpy as np


class KNNRegressorNumpy:
    """Minimal k-NN regressor for 1D input using NumPy."""

    def __init__(self, k: int):
        if k <= 0:
            raise ValueError("k must be a positive integer.")
        self.k = k
        self._X = None  # shape: (N,)
        self._y = None  # shape: (N,)

    def fit(self, X: np.ndarray, y: np.ndarray) -> "KNNRegressorNumpy":
        X = np.asarray(X, dtype=float).reshape(-1)
        y = np.asarray(y, dtype=float).reshape(-1)
        if X.shape[0] != y.shape[0] or X.shape[0] == 0:
            raise ValueError("X and y must be 1D arrays of the same non-zero length.")
        self._X = X
        self._y = y
        return self

    def predict(self, x_query: float) -> float:
        if self._X is None or self._y is None:
            raise RuntimeError("Model has not been fit yet.")
        # Compute absolute distances to the query
        dists = np.abs(self._X - float(x_query))

        # Get indices of the k smallest distances (stable tie-handling via argsort)
        # Using argsort here for simplicity and determinism on ties.
        nn_idx = np.argsort(dists)[: self.k]

        # k-NN regression => average y-values of the k nearest neighbors
        return float(np.mean(self._y[nn_idx]))


def read_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                print("Please enter a positive integer.", file=sys.stderr)
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.", file=sys.stderr)


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a number.", file=sys.stderr)


def main() -> None:
    print("=== k-NN Regression (NumPy, 1D) ===")
    N = read_positive_int("Enter N (number of points): ")
    k = read_positive_int("Enter k (neighbors): ")

    if k > N:
        print("Error: k must be less than or equal to N.", file=sys.stderr)
        return

    X_vals = np.empty(N, dtype=float)
    y_vals = np.empty(N, dtype=float)

    print("\nEnter the data points (x then y for each point):")
    for i in range(N):
        X_vals[i] = read_float(f"  x[{i+1}]: ")
        y_vals[i] = read_float(f"  y[{i+1}]: ")

    X_query = read_float("\nEnter query X: ")

    model = KNNRegressorNumpy(k=k).fit(X_vals, y_vals)
    y_pred = model.predict(X_query)

    # Print with reasonable precision
    print(f"\nPrediction for X = {X_query}: {y_pred:.6f}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAborted by user.", file=sys.stderr)
