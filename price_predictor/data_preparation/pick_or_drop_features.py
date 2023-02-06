import pandas as pd

anonymous_features = [ 'feature_0', 'feature_1', 'feature_2', 'feature_3', 
                      'feature_4', 'feature_5', 'feature_6', 'feature_7', 
                      'feature_8', 'feature_9']

categorical_features = ['manufacturer_name', 'model_name', 'transmission', 
                        'color', 'engine_fuel', 'engine_type', 'body_type',
                        'state', 'drivetrain', 'location_region']



    
def pick_by_datatypes(df: pd.DataFrame, features: list) -> pd.DataFrame:
    datatypes = []
    if 'numerical' in features:
        datatypes.append('int64')
        datatypes.append('float64')
        
    if 'boolean' in features:
        datatypes.append('bool')
        
    if 'categorical' in features:
        datatypes.append('object')
        
    return df.select_dtypes(datatypes)


def drop_anonymous_features(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop(anonymous_features, axis=1)


def drop_categorical_features(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop(categorical_features, axis=1)


def drop_by_name(df: pd.DataFrame, column: str) -> pd.DataFrame:
    return df.drop(column, axis=1)

def drop_categorical_except(df: pd.DataFrame, columns: list) -> pd.DataFrame: 
    return df.drop([feat for feat in categorical_features if feat not in columns], axis=1)

    