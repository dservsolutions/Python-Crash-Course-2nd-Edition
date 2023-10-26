# A simple example
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
    
# Checking Whether a Value Is not in List
# banned_users = ['andrew', 'carline', 'david']
# user = 'marie'

# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish. ")


# The if-elif-else Chain
# Example(1)
# age = 14
# if age < 4:
#     print("Your admission cost is 0$. ")
# elif age < 18:
#     print("Your admission cost is 25$. ")
# else:
#     print("Your admission cost is 40$. ")


# Testting Multiples Conditions

# requested_toppings =['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms. ")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese")

# print("\nFinished making your pizza.")

# # Using If Statements with List
# for requested_topped in requested_toppings:
#     print(f'Adding: {requested_topped}')
# print("Finished making your pizza")

# Checking that the list is no empty
# requested_toppings = []
# if requested_toppings:
#     for requested_topped in requested_toppings:
#         print(f"Adding {requested_toppings}")
#     print("\nFinished making your pizza!")

# else:
#     print("Are you sure want a plain pizza.")

# Using Multiple List
available_toppings = ['mushrooms', 'olives', 'green peppers', 
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry we don't have {requested_topping}") 
print("\n Finished making your pizza")