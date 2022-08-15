from enum import Enum

from .colors import *


colors = {
    "dell": Dell,
    "docker": Docker,
    "google": Google,
    "gravit": Gravit,
    "ikea": Ikea,
    "microsoft": Microsoft,
    "polaroid": Polaroid,
    "youtube": YouTube,

    "blue": Blue,
    "violet": Violet,
    "red": Red,
    "orange": Orange,
    "cyan": Cyan,
    "yellow": Yellow,
    "pink": Pink,
    "green": Green,
    "gray": Gray,

    "linkedine": LinkedInE,

    "experiment2": Experiment1,
    "experiment2": Experiment2
}


def get_colors(name: str) -> Enum:
    if name in colors:
        return colors[name]
    return None 
