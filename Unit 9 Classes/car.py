class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name. """
        long_name= f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement that showing the car mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    # Modifying an Attribute's Value Through a Method
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        # self.odometer_reading = mileage
        """
        Set the odometer reading to the given value.
        Reject the change if it attemps to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # Defining Attributes and Methods for the Child Class
        self.battery_size = 75

    # Defining a Method for the child class ElectricCar
    def describe_battery(self):
        """Print a statement describing the battery info"""
        print(f"This car has  a {self.battery_size}-kWh of battery")

    def get_range(self):
        """Print a statement about the range of this battery provide."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge. ")

# Making a new instance
# my_tesla = ElectricCar('Tesla', 'Model S', 2018)
# my_rivian = ElectricCar('Rivian', 'R1 S', 2022)




