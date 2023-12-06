# 9.4 Number Served
class Restaurant:
    # Init Method
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 10

    # Describe Restaurant Method
    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} offer {self.cuisine_type}")

    # Open Restauran Method
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")


# Creating a Instance
restauran = Restaurant('Juice Palace', 'Cuban Cuisine', 10)
print(f"{restauran.number_served} has been served. ")