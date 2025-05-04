# svg

[![MIT license][license-badge]][license-url]
[![Maintenance status][status-badge]][status-url]
[![Code coverage][coverage-badge]][coverage-url]

## About

**svg** is a python module and CLI application that will generate SVG based on yaml configuration file.

Also there is [todo list](./TODO.md).

## Motivation

Once I found nice image for wallpaper with graph. In fact two graphs or even four. Because one is pink and one is blue.

I would like to have different graph each time operating system is loaded.

That is why I started this project that became much more flexible that I expected.

## Requirements

Python version 3.8 or higher

Developed and tested on Ubuntu 20.04

## Installation

1. Clone the repo
    ```
    git clone https://github.com/vikian050194/svg.git
    ```
2. Install the package globally
    ```
    pip3 install .
    ```
3. Call installed package via a generated standalone "shim" script
    ```
    svg config.yaml
    ```
    or run Python module
    ```
    python3 svg config.yaml
    ```

## Development

```
virtualenv venv
source venv/bin/activate
pip install -e .
pip install -r reqirements/dev.txt
```

## Usage

**svg** needs yaml configuration file as a single argument.

Read the documentation to know how to generate wallpaper on system load.

### Automation

To install service and timer

```
bash automation/setup.sh
```

To remove it all

```
bash automation/clean.sh
```

## Documentation

Preparation

```
virtualenv venv
source venv/bin/activate
pip install -r reqirements/docs.txt
```

Live

```
mkdocs serve
```

Build

```
mkdocs build
```

## Tests

Module for testing is `unittest`

```
python3 -m unittest discover -t=. -s=tests/ -p=test_*.py
```

### Coverage

Preparation

```
virtualenv venv
source venv/bin/activate
pip install -r reqirements/docs.txt
```

Generate coverage results
```
coverage run -m unittest
```

To get total coverage percent
```
coverage report --format=total
```

To make text report
```
coverage report --format=text
```

To make HTML coverage report run following commands
```
coverage html
```

[status-url]: https://github.com/vikian050194/svg/pulse
[status-badge]: https://img.shields.io/github/last-commit/vikian050194/svg.svg

[license-url]: https://github.com/vikian050194/svg/blob/master/LICENSE
[license-badge]: https://img.shields.io/github/license/vikian050194/svg.svg

[coverage-url]: https://codecov.io/gh/vikian050194/svg
[coverage-badge]: https://img.shields.io/codecov/c/github/vikian050194/svg
