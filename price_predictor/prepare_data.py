import pandas as pd
from sklearn.model_selection import train_test_split


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
