import yaml

from sys import argv
from os import path, environ
from pathlib import Path


from svg.main import main
from svg.configuration import Configuration


def run():
    args = argv[1:]

    if len(args) != 1:
        print("ERROR: config file is not provided")
        return

    home = environ.get("SVG_HOME", None)

    if not home:
        home = Path.home().as_posix()
        home = path.join(home, "svg")

    configs = path.join(home, "configs")
    path_to_default_config_file = path.join(configs, "default.yaml")

    with open(path_to_default_config_file, "r") as stream:
        try:
            default_config_source = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    config_file_name = argv[1]
    path_to_config_file = path.join(home, config_file_name)

    with open(path_to_config_file, "r") as stream:
        try:
            config_source = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    width = config_source.get("width", default_config_source.get("width"))
    height = config_source.get("height", default_config_source.get("height"))
    palettes = config_source.get("palettes", default_config_source.get("palettes"))
    order = config_source.get("order", default_config_source.get("order"))
    patterns = config_source.get("patterns", default_config_source.get("patterns"))

    config = Configuration(home, width, height, palettes, order, patterns)

    main(config)


if __name__ == '__main__':
    run()
