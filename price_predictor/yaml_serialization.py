import yaml


def serialize_to_yaml(dictionary: dict, file_name: str, msg: str = None) -> None:
    file_name = "./config/" + file_name
    # File will be exporeted in a new folder named yaml
    with open(file_name, 'w+', encoding="utf-8") as file:
        if msg is not None:
             file.write(msg +'\n')
        else:
            file.write('# Allowed values are low-end / mid-end / high-end\n')
        yaml.dump(dictionary, file, allow_unicode=True)
        print(f"Exported dictionary to {file_name}")


# Load feature yaml files to dictionaries
def deserialize_make_yaml(file_name: str) -> None:
    with open(file_name, 'r', encoding='utf-8') as file:
        return yaml.load(file, Loader=yaml.FullLoader)
