# 9.13 Dice
import random

class Dice:
    
    def __init__(self, sides):
        self.sides = sides

    # Methods
    def roll_die(self):
        for _ in range(10):
            number = random.randint(1, self.sides)
            print(f"Dice roll:{number}")
        

# Making instances
dice_6 = Dice(sides= 6)
dice_6.roll_die()

dice_10 = Dice(sides= 10)
dice_10.roll_die()

dice_20 = Dice(sides=20)
dice_20.roll_die()
