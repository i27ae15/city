from enum import Enum, auto
from typing import TypedDict


class ColorClass(Enum):
    ROJO = auto()
    AMARILLO = auto()
    AZUL = auto()
    NEGRO = auto()


class MarcasClass(Enum):
    TOYOTA = auto()
    CHEVROLET = auto()
    FERRARI = auto()


class NumDoors(Enum):
    n_2 = 2
    n_4 = 4


class DiccDoor(TypedDict):
    COLOR: ColorClass


class DiccWheel(TypedDict):

    """
        {
            'MARCA': 'MarcasClass',
        }
    """

    MARCA: MarcasClass
    COLOR: ColorClass
