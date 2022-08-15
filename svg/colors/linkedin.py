from .base import Base


class Blue(Base):
    COLOR_A = "#CFEDFB"
    COLOR_B = "#9BDAF3"
    COLOR_C = "#68C7EC"
    COLOR_D = "#34B3E4"
    COLOR_E = "#00A0DC"
    COLOR_F = "#008CC9"
    COLOR_G = "#0077B5"
    COLOR_H = "#005E93"
    COLOR_I = "#004471"


class Violet(Base):
    COLOR_A = "#EBE4FF"
    COLOR_B = "#D8CCF4"
    COLOR_C = "#BFABE6"
    COLOR_D = "#A589D9"
    COLOR_E = "#8C68CB"
    COLOR_F = "#7C5BBB"
    COLOR_G = "#6A4BA7"
    COLOR_H = "#573B93"
    COLOR_I = "#452B7F"


class Red(Base):
    COLOR_A = "#FFE0DA"
    COLOR_B = "#FAC2BB"
    COLOR_C = "#F59890"
    COLOR_D = "#F16D64"
    COLOR_E = "#EC4339"
    COLOR_F = "#DD2E1F"
    COLOR_G = "#C11F1D"
    COLOR_H = "#A40F1C"
    COLOR_I = "#88001A"


class Orange(Base):
    COLOR_A = "#FFE7BB"
    COLOR_B = "#F8CD94"
    COLOR_C = "#F7B26A"
    COLOR_D = "#F59640"
    COLOR_E = "#EC4339"
    COLOR_F = "#EC640C"
    COLOR_G = "#CD5308"
    COLOR_H = "#AF4104"
    COLOR_I = "#903000"


class Cyan(Base):
    COLOR_A = "#D2ECEB"
    COLOR_B = "#9EDDDD"
    COLOR_C = "#69CDCF"
    COLOR_D = "#35BEC1"
    COLOR_E = "#00AEB3"
    COLOR_F = "#009EA5"
    COLOR_G = "#008891"
    COLOR_H = "#00727D"
    COLOR_I = "#005C69"


class Yellow(Base):
    COLOR_A = "#FFF2B6"
    COLOR_B = "#FBE491"
    COLOR_C = "#F7D56B"
    COLOR_D = "#F3C746"
    COLOR_E = "#EFB920"
    COLOR_F = "#E6A700"
    COLOR_G = "#CA9400"
    COLOR_H = "#AA7D00"
    COLOR_I = "#8B6700"


class Pink(Base):
    COLOR_A = "#FFDFF2"
    COLOR_B = "#FFC4E4"
    COLOR_C = "#F99ACA"
    COLOR_D = "#F371AF"
    COLOR_E = "#ED4795"
    COLOR_F = "#E2247F"
    COLOR_G = "#C9186E"
    COLOR_H = "#B10C5C"
    COLOR_I = "#870044"


class Green(Base):
    COLOR_A = "#E0F4BE"
    COLOR_B = "#C7E59A"
    COLOR_C = "#AED677"
    COLOR_D = "#95C753"
    COLOR_E = "#7CB82F"
    COLOR_F = "#60AA14"
    COLOR_G = "#4E8F13"
    COLOR_H = "#3B7511"
    COLOR_I = "#295A10"


class Gray(Base):
    COLOR_A = "#E6E9EC"
    COLOR_B = "#D0D3D6"
    COLOR_C = "#B6B9BC"
    COLOR_D = "#A0A3A6"
    COLOR_E = "#86898C"
    COLOR_F = "#737679"
    COLOR_G = "#595C5F"
    COLOR_H = "#434649"
    COLOR_I = "#303336"


class LinkedInE(Base):
    COLOR_A = Blue.COLOR_E.value
    COLOR_B = Violet.COLOR_E.value
    COLOR_C = Red.COLOR_E.value
    COLOR_D = Orange.COLOR_E.value
    COLOR_E = Cyan.COLOR_E.value
    COLOR_F = Yellow.COLOR_E.value
    COLOR_G = Pink.COLOR_E.value
    COLOR_H = Green.COLOR_E.value
    COLOR_I = Gray.COLOR_E.value


__all__ = [
    "Blue",
    "Violet",
    "Red",
    "Orange",
    "Cyan",
    "Yellow",
    "Pink",
    "Green",
    "Gray",
    "LinkedInE"
]
