#!/bin/env bash

. source/bin/activate
coverage run -m unittest discover -t=${workspaceFolder} -s=tests -p=test_*.py -v
coverage html