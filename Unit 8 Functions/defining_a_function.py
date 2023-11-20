# Defining a function
# def greet_user():
#     """Display a simple greeting."""
#     print("Hello")

# greet_user()

# Passing information to a function. 
# def greet_user(username):
#     print(f"Hello {username.title()}")

# greet_user('david') 

# Passing Arguments
# Positional Arguments
# def describe_pet(animal_type, pet_name):
#     """Display informatin about a pet."""
#     print(f"\nI have a {animal_type}. ")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet("dog", "lila")
# describe_pet(animal_type='cat', pet_name='cloe')

# Returning a Simple Value
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name.title()} {last_name.title()}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# Making a Argument Optional
# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted. """
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#         return full_name.title()
    
# actor = get_formatted_name("Jin", "carrey", "gonzalez")
# print(actor)
# men = get_formatted_name("Jimmy", "Fallen")
# print(men)

# Returning a Dictionary
# def build_person(first_name, last_name):
#     """Return a dictionary information about a person."""
#     person = {'first': first_name, 'last': last_name} 
#     return person

# musician = build_person(first_name='Jymmy', last_name='Fallen')
# print(musician) 

# Another Example
# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last':last_name, 'age':age}
#     if age:
#         person['age'] = age
#         return person

# musician = build_person('Yesse', 'Pedroso', 34)
# print(musician)

# Using a Function with a while loop
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted. """
#     full_name = f"{first_name} {last_name}."
#     return full_name.title()
        
# """This is a Infinite Loop"""
# while True:
#     print(f"\nPlease tell me your name: ")
#     print(f"\nPlease enter 'q' to exit ")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
    
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello {formatted_name}")

# Passing a List
# def greet_users(names):
#     """Print a simple greeting to each user in the list"""
#     for name in names:
#         msg = f"Hello {name.title()}!"
#         print(msg)

# username = ['david', 'diana', 'joseph', 'romeo']
# greet_users(username)

# Modifying a List in a Function
# Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# complete_models = []

# Simulating printing each design, until none are left
# Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     complete_models.append(current_design)

# # Display all complete models.
# print("\nThe following models have been printed:")
# for complete_model in complete_models:
#     print(complete_model)


# The same before example, but more organized using functions.
# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing models: {current_design}")
#         completed_models.append(current_design)
    

# def show_completed_models(completed_models):
#     print(f"\nThe following models have been printed: {completed_models}")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# Preventing a Funtion from Modifiying a List
# print_models(unprinted_designs[:], completed_models)

# Passing an Arbitrary Number of Arguments
# The asteric in the parameter name tells python to make a empty tuple calle toppings
# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested"""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushroom', 'green peppers', 'extra cheese')

# Other example using a foor loop
# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make"""
#     print("\nMaking a pizza with the following toppings: ")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'gree peppers', 'extra cheese')

# Mixing a Positional and Arbitrary Arguments
# def make_pizza(size, *toppings):
#     print(f"\nMaking a {size}-inch pizza with the following toppings: ")
#     for topping in toppings:
#         print(f"-{topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using Arbitrary Keywords Arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user. """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location= 'princeton', field='physics')

print(user_profile)

      