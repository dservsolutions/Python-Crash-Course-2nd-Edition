# 4.13 Buffet
basic_foods = ('omelet', 'bacon', 'chicken', 'pork', 'steak')

# (a)
print('Old Menu')
for food in basic_foods:
    print(food.title())

# (b)
# basic_foods[1] = 'rice'
# print(basic_foods[1])

# (c)
basic_foods_modified = ('omelet', 'bacon', 'chicken', 'pork', 'steak', 'rice')
print('New Menu')
for food in basic_foods_modified:
    print(food.title())

# 4.14 PEP 8
# 4.15
new_food_list = ('black beams', 'red beams', 'salad', 'spaguetti')



for food in new_food_list:
    print(food.title())