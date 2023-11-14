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
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted. """
    full_name = f"{first_name} {last_name}."
    return full_name.title()
        
"""This is a Infinite Loop"""
while True:
    print(f"\nPlease tell me your name: ")
    print(f"\nPlease enter 'q' to exit ")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello {formatted_name}")
