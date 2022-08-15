#!/usr/bin/env python3

import os

path_to_picture = f"{os.path.dirname(os.path.realpath(__file__))}/output.svg"
os.system(f"/usr/bin/gsettings set org.gnome.desktop.background picture-uri {path_to_picture}")
