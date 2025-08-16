from typing import TypedDict
from enums.sides import DiceFaces


class DiceSide(TypedDict):
    side_id: int
    die_side: DiceFaces
    weight: float
