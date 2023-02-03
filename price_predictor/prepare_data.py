import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

np.random.seed(42)

def get_numerical(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes(['int64', 'float64'])

def get_numerical_and_boolean(df: pd.DataFrame) -> pd.DataFrame:
    boolean_columns = df.select_dtypes(bool).columns
    df_numerical = get_numerical(df)
    df_boolean = _boolean_to_numerical(df, boolean_columns)
    data = pd.concat([df_numerical, df_boolean], axis=1)
    return data

def get_numerical_boolean_categorical(df: pd.DataFrame) -> pd.DataFrame:
    df_numerical_boolean = get_numerical_and_boolean(df)
    df_dummies = pd.get_dummies(df_numerical_boolean)
    return df_dummies    

def _boolean_to_numerical(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    return df[columns].applymap(lambda x: 1 if x else 0)

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