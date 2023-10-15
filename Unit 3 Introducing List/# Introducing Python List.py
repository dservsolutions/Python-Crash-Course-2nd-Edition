# Introducing Python List

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# Accessing Elements in a List
print(bicycles[0].title())

# Index Positions Start at 0, Not 1
print(bicycles[1])
print(bicycles[3])

# Accessing to the last item of the list
print(bicycles[-1])

# Using a Individual Values from a List
message = f'My first bicycle was a {bicycles[0].title()}'
print(message)

# Modifying Elements in a List
bicycles[0] = 'china_bicycle'
print(bicycles)

# Adding Element to a List(Appending elements to the End of the list)
bicycles.append('japan_bicycle')
print(bicycles)

# Inserting Elements into a List
bicycles.insert(0, 'cuban_bicycle')
print(bicycles)

# Removing Elements from a List(Using the del Statement)
del bicycles[0]
print(bicycles)
del bicycles[1]
print(bicycles)

# Removing a List item using the pop() method
motorcycles = ['vespino', 'honda', 'yamaha', 'suzuki']
popped_motorcyle = motorcycles.pop()
print(motorcycles)
print(popped_motorcyle)
print(f'The last mortorcycle I owned was a {popped_motorcyle.title()}')

# Popping Items from any Position in a List
first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned}')

# Removing a item by value using remove method
motorcycles.remove('honda')
print(f'Is most expensive and not realiable that {motorcycles}')