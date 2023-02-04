from argparse import ArgumentParser
from price_predictor.yaml_serialization import serialize_to_yaml


# Create yaml file that has all unique values in a dictionary for a specific feature
def create_feature_template_yaml(make_list: list, file_name: str, msg=None) -> None:
    make_dictonary = {key: "" for key in make_list}
    serialize_to_yaml(make_dictonary, file_name, msg)


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('--make-list', nargs='+', type=list, required=True, dest='make_list')
    parser.add_argument('--dest', type=str, required=True)
    parser.add_argument('--msg', type=str, required=False, default=None)

    args = parser.parse_args()

    if args.msg:
        create_feature_template_yaml([''.join(word) for word in args.make_list], args.dest, args.msg)
    else:
        create_feature_template_yaml(args.make_list, args.dest)


main()
