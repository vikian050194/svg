#!/usr/bin/env python3

import yaml

from sys import argv
from os import environ
from pathlib import Path

from svg import main
from svg.configuration import Configuration


if __name__ == "__main__":
    home = Path.home().as_posix()
    home = environ.get("SVG_HOME", home)

    config_file_name = environ.get("SVG_CONFIG", "config.yaml")
    config_file_name = argv[1] if len(argv) == 2 else config_file_name

    with open(config_file_name, "r") as stream:
        try:
            config_source = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    width = config_source["width"]
    height = config_source["height"]
    palette = config_source["palette"]
    order = config_source["order"]
    patterns = config_source["patterns"]

    config = Configuration(home, width, height, palette, order, patterns)

    main(config)
