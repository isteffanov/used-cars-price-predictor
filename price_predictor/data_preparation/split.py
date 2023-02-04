import pandas as pd
from sklearn.model_selection import train_test_split, KFold

from typing import Generator

def split_train_test_valid(df: pd.DataFrame) -> tuple:
    train_valid_data, test_data = train_test_split(df, test_size=0.1)
    train_data, valid_data = train_test_split(train_valid_data, test_size=0.5)

    train_features, train_target = _split_features_target(
        pd.DataFrame(train_data, columns=df.columns), 
        'price_usd')
    valid_features, valid_target = _split_features_target(
        pd.DataFrame(valid_data, columns=df.columns), 
        'price_usd')
    test_features, test_target = _split_features_target(
        pd.DataFrame(test_data, columns=df.columns), 
        'price_usd')
    
    return (
        train_features, 
        test_features, 
        valid_features, 
        train_target,
        test_target,
        valid_target
    )

def _split_features_target(df: pd.DataFrame, target: str) -> tuple:
    X = df.drop(target, axis=1, inplace=False)
    y = df[target]
    
    return X, y


def kfold_train_test(
    df: pd.DataFrame, 
    n_splits: int) -> Generator[tuple, None, None]:
    
    kf = KFold(n_splits=n_splits)
    for train_index, test_index in kf.split(df):
        yield (_split_features_target(df.iloc[train_index], 'price_usd'),
               _split_features_target(df.iloc[test_index], 'price_usd'))
    