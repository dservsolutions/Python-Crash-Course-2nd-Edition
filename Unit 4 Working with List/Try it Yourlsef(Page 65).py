 
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# (a)
print(f'The first three items in the list are:{players[0:3]}')

# (b)
print(f'Three items from the middle of the list are:{players[1:4]}')

# (c)
print(f'The last three items of the list are: {players[:3]}')

# 4.11 My Pizzas, Your Pizzas
list_of_pizzas = ['pepperoni', 'napolitana', 'hawaiian', 'margherita', 'veggie']
friend_pizzas = list_of_pizzas[:]

# (a)
list_of_pizzas.append('cuban')

# (b)
friend_pizzas.append('deep dish')

# (c)
print("My favorite pizzas are: ")
for pizza in list_of_pizzas:
    print(pizza)

print("My friend's favorite pizzas are: ")
for fpizzas in friend_pizzas:
    print(fpizzas)

# 4.12 More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
print(" My favorite foods are: ")
for food in my_foods:
    print(food)

favorite_foods = [food for food in my_foods]
print(favorite_foods)