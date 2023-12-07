from restaurant import Restaurant
from users import User

# 9.6 Ice Cream Stand:
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'chocolate chip', 'strawverry',
                         'coffee', 'pistachio', 'neapolitan']
        
    def display_flavors(self):
        """Showing ice cream flavors."""
        print("These are the flavor available:")
        for flavors in self.flavors:
            print(flavors)

# Making an instance of IceCreamStand
icecream = IceCreamStand('Wendys', 'American Cuisine')

# icecream.display_flavors()

# 9.7 Admin
class Admin(User):
    """Inherit of User Class"""
    def __init__(self, first_name, last_name, email):
        self.firstname = first_name
        self.lastname = last_name
        self.email = email
        self.privileges = ["can add post", "can delete post", "can ban user"]

    # # Method that show the user privileges.
    # def show_privileges(self):
    #     print(f"{self.firstname.title()} has the followings privileges:")
    #     for privilege in self.privileges:
    #         print(privilege.title())

# Making a instance
user_privileges = Admin('David', 'Pedroso', 'ppdavisito89@outlook.es')
user_privileges.describe_user()

# 9.8 Privileges
class Privileges:
        def __init__(self):
             self.privileges_list = ["can add post", "can delete post", "can ban user"]

    # Method that show the user privileges.
        def show_privileges(self):
             print("Has the followings privileges:")
             for privilege in self.privileges_list:
                print(privilege.title())





    


