# Unit  Working with List
# Looping through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print (magician)

# Doing more work Withing a for Loop
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick!,{magician.title()}.\n")

# Doing something After a for Loop
print("Thank you, everyone. That was a great magic show! ")

# Avoiding Indentation Errors
# Makin numerical list
# Using range() function
for value in range(1, 5):
    print(value)

# Using range to make a List of Number
number = list(range(1, 6))
print(number)
# If you pass a third argument to range(), Python uses that value as a step size.
even_number = list(range(2, 11, 2))
print(even_number)

# Square numbers
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

# List Comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)

# Working with a Part of a List
# Slicing in a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[3:])
print(players[-3:])

# Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the firts three players on my team: ")
for player in players[:3]:
    print(player.title())

# Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print(f'My favorite foods are:')
print(my_foods)
print('My friends favorite foods are: ')
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(f'My favorite foods are:')
print(my_foods)
print('My friends favorite foods are: ')
print(friend_foods)

# Tuples