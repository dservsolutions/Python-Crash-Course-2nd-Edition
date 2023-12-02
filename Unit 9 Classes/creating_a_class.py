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