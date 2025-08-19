from dice import Die

class DiceArray:
    num_dice: int
    dice_list: list[Die]

    # default constructructor
    def __init__(self):
        self.num_dice = 6
        for i in range(self.num_dice):
            self.dice_list.append(Die())
        