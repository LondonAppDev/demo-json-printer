import json


def path_to_dict(path):
    """Open file at provided path and return as dictionary."""
    with open(path) as json_file:
        json_dict = json.load(json_file)


def print_values(input_dict):
    """Loop through dictionary and print values."""
    for k, v in input_dict.items():
        print('{0}: {1}'.format(k, v))


def main():
    """Entrypoint to application."""
    sample_dict = path_to_dict('sample.json')
    print_values(sample_dict)


if __name__ == '__main__':
    main()
