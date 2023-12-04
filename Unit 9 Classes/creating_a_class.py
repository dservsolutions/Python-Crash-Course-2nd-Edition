# Creating and Using a Class
class Dog:
    """A simple attemp to model a dog."""
    def __init__(self, name, age) -> None:
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over! ")


# Making a instance from a class
my_dog = Dog('Rocky', 7)

# Accesing Attributes
print(f"My dog names is {my_dog.name} and is {my_dog.age} old.")

# Calling Methods
my_dog.sit()
my_dog.roll_over()

# Creating Multiple Instances
neigbornhood_dog = Dog('Jason', 3)
friend_dog = Dog('Bell', 3)


print(f"My friend dog name's {friend_dog.name} and is {friend_dog.age} years old")
friend_dog.sit()
friend_dog.roll_over()



# Working with Classes and Instances 
# The Car Class

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


    
# Creating an instance
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# Setting a Default Value for an attribute
my_new_car.read_odometer()

# Modifying attributes values
# Modifying an Attribute Value Directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# Modifying an Attribute's Value Through a Method(Getting the response of the change)
my_new_car.update_odometer(32)
my_new_car.read_odometer()

my_new_car.update_odometer(10)
my_new_car.read_odometer()


# Incrementing an Attribute's Values throught a Method
my_user_car = Car('Subaru', 'Outback', 2015)
print(my_user_car.get_descriptive_name())

my_user_car.update_odometer(23_500)
my_user_car.read_odometer()

my_user_car.increment_odometer(100)
my_user_car.read_odometer()