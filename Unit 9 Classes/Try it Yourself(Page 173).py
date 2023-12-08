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

# 9.7 Admin
class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        # self.priv = Privileges()
        
    # Making an instance
admin = Admin('david', 'pedroso', 'hola@gmail.com')


# 9.8 Privileges
class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    # Method
    def show_privileges(self):
        print("Administrator's set of privileges:")
        for privilege in self.privileges:
            print(privilege.title())

# 9.9 Battery Upgrade
class Battery(ElectricCar):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 100

    # Method Upgrade Battery    
    def upgrade_battery(self, battery_size):
        if self.battery_size != 100:
            print(f"Battery size: {battery_size}-kWh and isn't ready. ")

# Making a instance
my_car = Battery('tesla', 'model 1s', 2022)
my_friend_car = Battery('rivian', 'r1', 2023)
my_friend_car.get_range()
    





    


