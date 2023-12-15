# 9.13 Dice
import random

class Die:
    
    def __init__(self):
        self.sides = 6
    # Methods
    def roll_die(self):
        sides = random.randint(1, self.sides)
        for sides in range(1, 9):
            print(sides)

# Making a instance
die = Die()
die.roll_die()
