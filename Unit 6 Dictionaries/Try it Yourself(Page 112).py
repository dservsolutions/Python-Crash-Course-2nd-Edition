# 6.7 People

person_0 = {'first_name': 'maria',
          'last_name': 'caridad',
          'age': '65',
          'city': 'havana'}

person_1 = {'first_name': 'daniel',
          'last_name': 'garcia',
          'age': '45',
          'city': 'havana'}

person_2 = {'first_name': 'daniel',
          'last_name': 'elias',
          'age': '45',
          'city': 'havana'}

peoples = [person_0, person_1, person_2]
# persons = [ people for people in peoples]
for people in peoples:
    print(f"Name: {people['first_name'].title()} {people['last_name'].title()} Age:{people['age']} City:{people['city'].title()}")
