# 9.1 Restaurant
# Creating a Class Restaurant
class Restaurant:
    # Init Method
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # Describe Restaurant Method
    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} offer {self.cuisine_type}")

    # Open Restauran Method
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

# Making a instance called restaurant
rest_0 = Restaurant('Sakura', 'Japanese Cuisine')

print(f"The restaurant name's {rest_0.restaurant_name.title()}")
print(f"{rest_0.restaurant_name.title()} is open.")

rest_0.describe_restaurant()
rest_0.open_restaurant()

# 9.2 Three Restaurants
rest_1 = Restaurant('Don Maguey', 'Mexican Cousine')
rest_2 = Restaurant('La Nueva', 'Salvador Cuisine')
rest_3 = Restaurant('Las Cubanitas', 'Cuban Cuisine')

for rest in rest_1, rest_2, rest_3:
    rest.describe_restaurant()


# 9.3 Users
# Creating a class User
class User:
    def __init__(self, first_name, last_name, email):
        self.firstname = first_name
        self.lastname = last_name
        self.email = email
    # Method Describe User
    def describe_user(self):
        print(f"Name: {self.firstname.title()}\n")
        print(f"Lastname: {self.lastname.title()}\n")
        print(f"Email: {self.email}")
    # Method Greet User 
    def greet_user(self):
        print(f"Welcome {self.firstname}")

# Making Instances
user_0 = User('pedro', 'lada fonseca', 'pedrito1234@gmail.com')
user_1 = User('jose', 'alfonso garcia', 'jose222.@hotmail.com')
user_2 = User('jhon', 'wick enough', 'jhon_wick2024@proton.com')
        
for users in user_0,user_1, user_2:
    users.describe_user()