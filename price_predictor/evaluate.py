import numpy as np
from sklearn.metrics import (
    mean_squared_error,
    accuracy_score,
    r2_score
)

def evaluate(y_true: list, y_pred: list) -> dict:
    return {
        'accuracy': accuracy_score(y_true, y_pred),
        'mse': mean_squared_error(y_true, y_pred),
        'r2': r2_score(y_true, y_pred)
    }