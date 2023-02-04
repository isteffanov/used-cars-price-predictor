from pandas import DataFrame
from sklearn.linear_model import LinearRegression, LassoCV, RidgeCV

def train_linear_regression(X_train: DataFrame, y_train: DataFrame, *args, **kwargs) -> LinearRegression:
    linear_regression = LinearRegression(*args, **kwargs)
    linear_regression.fit(X_train, y_train)
    return linear_regression

def train_lasso_cv(X_train: DataFrame, y_train: DataFrame, *args, **kwargs) -> LassoCV:
    lasso = LassoCV(*args, **kwargs)
    lasso.fit(X_train, y_train);
    return lasso

def train_ridge_cv(X_train: DataFrame, y_train: DataFrame, *args, **kwargs) -> RidgeCV:
    ridge = RidgeCV(*args, **kwargs)
    ridge.fit(X_train, y_train);
    return ridge