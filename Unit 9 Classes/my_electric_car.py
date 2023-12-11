from car import ElectricCar

my_tesla = ElectricCar('Tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.get_range()