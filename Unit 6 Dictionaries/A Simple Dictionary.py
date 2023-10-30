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