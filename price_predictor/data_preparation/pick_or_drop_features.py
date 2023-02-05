import pandas as pd

anonymous_features = [ 'feature_0', 'feature_1', 'feature_2', 'feature_3', 
                      'feature_4', 'feature_5', 'feature_6', 'feature_7', 
                      'feature_8', 'feature_9']


    
def pick_by_datatypes(df: pd.DataFrame, features: list) -> pd.DataFrame:
    datatypes = []
    if 'numerical' in features:
        datatypes.append('int64')
        datatypes.append('float64')
        
    if 'boolean' in features:
        #boolean_columns = df.select_dtypes(bool).columns
        #df[boolean_columns] = df[boolean_columns].applymap(lambda x: 1 if x else 0)
        
        datatypes.append('bool')
        
    if 'categorical' in features:
        datatypes.append('object')
        
    return df.select_dtypes(datatypes)

def drop_anonymous_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop(anonymous_features, axis=1)

def drop_by_name(df: pd.DataFrame, column: str) -> pd.DataFrame:
    return df.drop(column, axis=1)
    