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
# dice_6 = Dice(sides= 6)
# dice_6.roll_die()

# dice_10 = Dice(sides= 10)
# dice_10.roll_die()

# dice_20 = Dice(sides=20)
# dice_20.roll_die()


# 9.14 Lottery
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e', 'f')
random_items = random.sample(numbers, 4)


# 9.15 Lottery Analysis:
# Tuple
my_ticket = (2, 3, 4, 'a')
counter = 0
while True:
    for items in random_items:
        counter +=1
        print(f"The loop had run: {counter} times.")
        for ticket in my_ticket:
            if ticket == items:
                break
         
       
