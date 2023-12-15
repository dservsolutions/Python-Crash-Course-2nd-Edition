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
numbers = (1, 12, 14, 22, 33, 44, 51, 61, 88, 102, 'a', 'b', 'c', 'd', 'e', 'f')
random_items = random.sample(numbers, 4)
# print(f"None ticket match with these charapters: ")
# for items in random_items:
#     print(items)

# 9.15 Lottery Analysis:
my_ticket = (12, 1, 33, 'a')
stop = False
while stop:
    for items in random_items:
        print(items)
       
