from random import random
from enums.sides import DiceFaces
from typeInterfaces.diceSideType import DiceSide


class Die:
    #  defaults

    num_sides: int = 6
    auto_increment_id: int = 0
    dice_sides: list[DiceSide] = []

    def __init__(self):
        self.num_sides: int = 6
        self.dice_sides: list[DiceSide] = [
            {'side_id': 1, "die_side": DiceFaces.ONE, "weight": 1},
            {'side_id': 2, 'die_side': DiceFaces.TWO, 'weight': 1},
            {'side_id': 3, 'die_side': DiceFaces.THREE, 'weight': 1},
            {'side_id': 4, 'die_side': DiceFaces.FOUR, 'weight': 1},
            {'side_id': 5, 'die_side': DiceFaces.FIVE, 'weight': 1},
            {'side_id': 6, 'die_side': DiceFaces.SIX, 'weight': 1}
        ]
        self.auto_increment_id = 7

    def add_side(self, side_face: DiceFaces = DiceFaces.WILDCARD, weight: float = 1):
        self.dice_sides.append(
            {'side_id': self.auto_increment_id, 'die_side': side_face, 'weight': weight}
        )
        self.auto_increment_id += 1

    def remove_side(self, side_id: int):
        self.dice_sides = [
            side for side in self.dice_sides if side['side_id'] != side_id]

    def modify_side(self, side_id: int, side_face: DiceFaces, weight: float):
        for side in self.dice_sides:
            if side['side_id'] == side_id:
                side['die_side'] = side_face
                side['weight'] = weight
                break

    def roll(self) -> DiceFaces:
        from random import choices
        return choices([side['die_side'] for side in self.dice_sides],
                       weights=[side['weight'] for side in self.dice_sides])[0]
