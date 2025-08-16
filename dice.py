from random import random
from enums.sides import DiceFaces
from typeInterfaces.diceSideType import DiceSide


class Die:
    #  defaults

    num_sides: int = 6
    dice_sides: list[DiceSide] = []

    def __init__(self):
        self.num_sides: int = 6
        self.dice_sides: list[DiceSide] = [
            {"die_side": DiceFaces.ONE, "weight": 1},
            {'die_side': DiceFaces.TWO, 'weight': 1},
            {'die_side': DiceFaces.THREE, 'weight': 1},
            {'die_side': DiceFaces.FOUR, 'weight': 1},
            {'die_side': DiceFaces.FIVE, 'weight': 1},
            {'die_side': DiceFaces.SIX, 'weight': 1}
        ]

    def roll(self) -> DiceFaces:
        from random import choices
        return choices([side['die_side'] for side in self.dice_sides],
                       weights=[side['weight'] for side in self.dice_sides])[0]
