import numpy as np
from pandas import DataFrame
from sklearn.base import BaseEstimator
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

def evaluate_model(
    model: BaseEstimator,
    X_test: DataFrame,
    y_test: DataFrame) -> dict:
    
    y_pred = model.predict(X_test)
    return evaluate(y_test, y_pred)

def evaluate(y_true: list, y_pred: list) -> dict:
    return {
        # 'accuracy': accuracy_score(y_true, y_pred),
        'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
        'mae': mean_absolute_error(y_true, y_pred),
        'r2': r2_score(y_true, y_pred)
    }