from restaurant import Restaurant
from users import User
from inheritance import ElectricCar

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
             self.privileges_list = ["can add post", "can delete post", "can ban user"]

    # Method that show the user privileges.
        def show_privileges(self):
             print("Has the followings privileges:")
             for privilege in self.privileges_list:
                print(privilege.title())

# 9.7 Admin
class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.pri = Privileges()
        
    # Making an instance
admin = Admin('david', 'pedroso', 'ppdavisito89@outlook.es')


# 9.9 
class Battery(ElectricCar):
     def __init__(self, make, model, year):
          super().__init__(make, model, year)
          self.battery_size = 100

        # Method Upgrade Battery
     def upgrade_battery(self):
         if self.battery_size != 100:
          print("The battery need to be upgrade.")
          self.battery_size = 100
         else:
             print("The battery is ready.")

# Making a new instance
my_car = Battery('Rivian', 'R1s', 2022)
my_car.describe_battery()







    


