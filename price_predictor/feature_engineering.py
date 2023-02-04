import pandas as pd
from price_predictor.yaml_serialization import serialize_to_yaml, deserialize_make_yaml

#todo
def create_make_model_yaml(make_model_list: list, file_name: str, msg=None) -> None:
    make_model_dict = {key: "" for key in make_model_list}
    serialize_to_yaml(make_model_dict, file_name, msg)


def populate_feature_template_to_dataframe(df: pd.DataFrame, column_name_result, column_name_map, file_name:str) -> pd.DataFrame:
    # Load information from yaml file
    make_dict = deserialize_make_yaml(file_name)
    df[column_name_result] = df[column_name_map].map(make_dict)
    return df

