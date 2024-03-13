import random

class Dice:
    """A class for rolling various dice"""
    
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        """Rolls the die and returns the result"""
        return random.randint(1, self.sides) 
    