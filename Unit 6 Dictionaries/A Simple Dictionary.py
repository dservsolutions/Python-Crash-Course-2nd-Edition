alien_0 = {
    'color': 'green',
    'points': '5'
}

print(alien_0['color'])


# Working with Dictionaries
new_point = alien_0['points']
print(f"You just earn: {new_point} points!")

# Addin New Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# Starting wiht a empty dictionary
alien_1 = {}
alien_1['color'] = 'blue'
alien_1['points'] = '25'

print(alien_1)

# Modifying Values in a Dictionary
alien_1 = {'color': 'green'}
print(f'The alien is {alien_1["color"]}.')

alien_1['color'] = 'yellow'
print(f'The alien is now {alien_1["color"]}')


# Another Example
alien_3 = {'x_position': 0,
           'y_position': 25,
           'speed': 'medium'}
print(f"Original Position: {alien_3['x_position']}")

# Moving the alien to the right
# Determine how far to move
if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 3
else:
    #This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_3['x_position'] = alien_3['x_position'] + x_increment
print(f"New position: {alien_3['x_position']}")


# Removing Key-Value Pairs
alien_4= {'color': 'acuarine',
          'points': '25'}
del alien_4['points']
print(alien_4)

# A Dictionary with Similar Objects
favorite_languages = {'jen': 'python',
                      'sarah': 'C',
                      'edward': 'ruby',
                      'phil': 'pyhthon'}

language = favorite_languages['sarah']

print(f"Sarah's favorite language is {language}")

# Using get() to Access Values
alien_5 = {'color': 'white', 'speed': 'slow'}
point_value = alien_5.get('points', 'No point value assigned. ')
print(point_value)


# Looping through All Key-Value Pairs
# for key, value in favorite_languages.items():
#     print(f"Name: {key}, Favorite Language: {value}")


# for name in favorite_languages.keys():
#     print(f"Name:{name}")


# friends = ['jhon', 'pedro', 'sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}! ")
    
# if 'erin' not in favorite_languages.keys():
#     print(f"Erin, please take our poll! ")

# Looping through a Dictionary's Keys in a Particular Order.
for names in sorted(favorite_languages.keys()):
    print(f"{names.title()}, thank your for taking the poll")


# Looping throught All Values in a Dictionary
# print("The following programming languages have been mentioned")
# for language in favorite_languages.values():
#     print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())

