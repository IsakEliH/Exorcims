import random

class Character:
    def __init__(self):

        def three_dice():      
            four_dice = [random.randint(0,6) for _ in range(4)]
            minimum = min(four_dice)
            four_dice.remove(minimum)
            return four_dice

        self.strength = sum(three_dice())
        self.dexterity = sum(three_dice())
        self.constitution = sum(three_dice())
        self.intelligence = sum(three_dice())
        self.wisdom = sum(three_dice())
        self.charisma = sum(three_dice())

        self.hitpoints = 10 + ((self.constitution - 10) // 2)

    def ability(self):
        """Return a random ability score between 3 and 18."""
        four_dice = [random.randint(1, 6) for _ in range(4)]
        four_dice.remove(min(four_dice))
        return sum(four_dice)


def modifier(value):
    return ((value - 10) // 2)
