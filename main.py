from dice import Die

if __name__ == "__main__":
    die = Die()
    die.remove_side(1)
    die.remove_side(2)
    die.remove_side(3)
    die.remove_side(4)
    die.add_side()
    print(die.roll())
    print(die.roll())
    print(die.roll())
    print(die.roll())
    print(die.roll())
