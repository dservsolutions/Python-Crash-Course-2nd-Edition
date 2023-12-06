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

# 9.8 Privileges
class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    # Method
    def show_privileges(self):
        print("Administrator's set of privileges:")
        for privilege in self.privileges:
            print(privilege.title())

# 9.7 Admin
class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.pri = Privileges()
        
    # Making an instance
admin = Admin('david', 'pedroso', 'ppdavisito89@outlook.es')





    


