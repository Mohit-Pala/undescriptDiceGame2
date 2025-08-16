from typing import TypedDict
from enums.sides import DiceFaces


class DiceSide(TypedDict):
    die_side: DiceFaces
    weight: float
