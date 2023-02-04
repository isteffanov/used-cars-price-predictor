from pandas import DataFrame
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.model_selection import GridSearchCV

def train_random_forest(
    X_train: DataFrame,
    y_train: DataFrame,
    *args, 
    **kwargs) -> RandomForestRegressor:
    
    random_forest = RandomForestRegressor(*args, **kwargs)
    random_forest.fit(X_train, y_train)
    return random_forest
    
   
def search_random_forest(
    X_train: DataFrame,
    y_train: DataFrame,
    *args, 
    **kwargs) -> GridSearchCV:
    
    random_forest_search = GridSearchCV(RandomForestRegressor(), *args, **kwargs)
    random_forest_search.fit(X_train, y_train)
    return random_forest_search 
    

def train_ada_boost(
    X_train: DataFrame,
    y_train: DataFrame,
    *args, 
    **kwargs) -> AdaBoostRegressor:
    
    ada_boost = AdaBoostRegressor(*args, **kwargs)
    ada_boost.fit(X_train, y_train)
    return ada_boost

def search_ada_boost(
    X_train: DataFrame,
    y_train: DataFrame,
    *args, 
    **kwargs) -> GridSearchCV:
    
    ada_boost_search = GridSearchCV(AdaBoostRegressor(), *args, **kwargs)
    ada_boost_search.fit(X_train, y_train)
    return ada_boost_search 