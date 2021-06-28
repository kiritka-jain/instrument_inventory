from enum import Enum


class Wood(Enum):
    INDIAN_ROSEWOOD = 'indian_rosewood'
    MAHAGONY = 'mahagony'


class Type(Enum):
    ELECTRIC = 'electric'
    AUCOUSTIC = 'aucoustic'
    OCTAVE = 'octave'


class Builder(Enum):
    FENDER = 'fender'
    MARTIN = 'martin'


class Style(Enum):
    A_STYLE = 'a_style'
    F_STYLE = 'f_style'
