# 6.1 Person

person = {'first_name': 'daniel',
          'last_name': 'garcia',
          'age': '45',
          'city': 'havana'}
print(person['first_name'].title(), person['last_name'].title())

# 6.2 Favorite Number

favorite_numbers = {'david': '3',
                    'jhon': '5',
                    'dave': '6',
                    'michael': '7',
                    'paolo': '10'}

print(favorite_numbers)

# 6.3 Glossary
# (a)
glossary = {'list': 'Used to store multiple items in a single variable',
            'tuple': 'Tuple is one of 4 built-in data types in Python used to store collections of data',
            'boolean': 'represents one of the two values i.e. True or False',
            'while loop': 'a control flow statement which allows code to be executed repeatedly, depending on whether a condition is satisfied or not',
            'function': 'a block of code which only runs when it is called'
            }

# for key, value in glossary.items():
#     print(key.title(), value.title())

# 6.4 Glossary 2
for words, meanings in glossary.items():
    print(f"{words.title()}: {meanings.title()}")

# 6.5 Rivers 
rivers = {'nylo': 'egypt',
          'missisipi': 'united states',
          'cauto': 'cuba'}

# for names, countries in rivers.items():
#     #(a)
#     print(f"The {names.title()}, runs throught {countries.title()}")

# #(b)
# for names in rivers.keys():
#     print(names.title())

# #(c)
# for countries in rivers.values():
#     print(countries.title())

# 6.6 Polling
# (a)
favorite_languages = {'jen': 'python',
                      'sarah': 'C',
                      'edward': 'ruby',
                      'phil': 'pyhthon'}

list_names = ['pepa', 'jhosep', 'alan', 'phil', 'edward']

for names in list_names:
    if names in favorite_languages.keys():
        print(f"Thanks {names.title()}, for taking the poll. ")
    else:
        print(f"{names.title()}, You're invited to take the poll.")

