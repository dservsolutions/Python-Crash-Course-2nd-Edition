# 9.4 Number Served
class Restaurant:
    # Init Method
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.people_served = 0

    # Describe Restaurant Method
    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} offer {self.cuisine_type}")

    # Open Restauran Method
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    # Set number of customers served
    def number_served(self, qty_served):
        self.people_served = qty_served
        print(f"The number of people served is: {self.people_served}")

    # Incrementing the number of people served
    def increment_number_served(self, new_value):
        new_value += self.people_served
        print(f"The total of customer served is: {new_value}")

# Creating a Instance
restauran = Restaurant('Juice Palace', 'Cuban Cuisine')
restauran.number_served(qty_served=25)
restauran.increment_number_served(15)

# 9.5 Login Attemps
class User:
    def __init__(self, first_name, last_name, email):
        self.firstname = first_name
        self.lastname = last_name
        self.email = email
        self.login_attemps = 0

    # Method Describe User
    def describe_user(self):
        print(f"Name: {self.firstname.title()}")
        print(f"Lastname: {self.lastname.title()}")
        print(f"Email: {self.email}")
        
    # Method Greet User 
    def greet_user(self):
        print(f"Welcome {self.firstname}")
        print(f"Login Attemps: {self.login_attemps}")

    def increment_login(self, login):
        self.login_attemps += login

    def reset_login_attemps(self):
        if self.login_attemps:
            reset = self.login_attemps - self.login_attemps
            print(f"New Login Attemps: {reset}")


login = True
stud_0 = User('David', 'Pedroso', 'asd@gmail.com')
while login:
    stud_0.describe_user()
    stud_0.increment_login(1)
    stud_0.greet_user()
    if stud_0.login_attemps == 5:
        print("You have three login attemps")
        login == False
        break

reset_login = input("Would you like reset your logging attemps? Write (Y/N): ")
if reset_login.title() == "Y":
    stud_0.reset_login_attemps()
else:
    stud_0.greet_user()










