
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



