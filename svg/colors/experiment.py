from .base import Base


class Experiment1(Base):
    COLOR_A = "#003467"
    COLOR_B = "#02447B"
    COLOR_C = "#346FB0"
    COLOR_D = "#FFC637"
    COLOR_E = "#C1000F"


class Experiment2(Base):
    COLOR_A = "#86E3CE"
    COLOR_B = "#D0E6A5"
    COLOR_C = "#FFDD94"
    COLOR_D = "#FA897B"
    COLOR_E = "#CCABD8"


__all__ = [
    "Experiment1",
    "Experiment2"
]
