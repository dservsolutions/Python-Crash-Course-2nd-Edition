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
def describe_pet(animal_type, pet_name):
    """Display informatin about a pet."""
    print(f"\nI have a {animal_type}. ")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet("dog", "lila")
describe_pet(animal_type='cat', pet_name='cloe')