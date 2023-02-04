from pandas import DataFrame
from sklearn.base import BaseEstimator
from sklearn.metrics import (
    mean_squared_error,
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
        'mse': mean_squared_error(y_true, y_pred),
        'r2': r2_score(y_true, y_pred)
    }