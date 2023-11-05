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


# 6.8 Pets

pet_01 = {'kind': 'dog',
          'owner name': 'jhony'}

pet_02 = {'kind': 'cat',
          'owner name': 'david'}

pet_03 = {'kind': 'carrot',
          'owner name': 'juan'}

pet_04 = {'kind': 'monkey',
          'owner name': 'jhon'}

pets_lst = [pet_01, pet_02, pet_03, pet_04]

for pet in pets_lst:
    print(f"The {pet['kind'].title()},owner's name is {pet['owner name'].title()}")


# 6.9 Favorite Places

favorite_place = {'jhon': 'rome, milan, venecia',
                  'juan': 'greece, island, panama',
                  'robert': 'toronto, vancouver, halifax'}

places_lst = [favorite_place]

# name = input("Enter your name, please: ")

# for names in places_lst:
#     if name in names:
#         print(f"{name.title()}'s favorite places are : {names[name].title()}.")
#     else:
#         print(f"{name} isn't in the list")


# 6.10 Favorite Numbers.
favorite_numbers = {'david': '3, 9, 11',
                    'jhon': '5',
                    'dave': '6',
                    'michael': '7',
                    'paolo': '10'}
fav_lst = [favorite_numbers]


for name, numbers in favorite_numbers.items():
        print(f"{name.title()} favorite's number are {numbers}")

# 6.11 Cities
cities = {
     'miami': {
          'country': 'USA',
          'population': '2,673,837',
          'fact': 'It is the only US city that was founded by a woman'
     },
     'caracas': {
          'country': 'Venezuela',
          'population': '2,901,918',
          'fact': 'The vibrant and bustling capital city of Venezuela'
     },
     'havana': {
        'country':  'Cuba',
        'population': '2,149,000',
        'fact': 'Havana was founded in 1519'
     }
}

for city, info in cities.items():
     print(f"{city.title()}")
     info_city = f"Country:{info['country']}, Population: {info['population']}, Fun Fact: {info['fact']}\n" 
     print(info_city)


# 6.12 Extensions: 
invited_dict = {
     'david':{
          'Age': 34,
          'Vehicle': 'Bike'
     },
     'carmen': {
          'Age': 55,
          'Vehicle': 'Car'
     },
     'jhonny': {
          'Age': 43,
          'Vehicle': 'Car'
     },
     'arthur': {
          'Age': 65,
          'Vehicle': 'Bicycle'
     },

}

no_invited_lts = []

name = input("Please enter your name: \n")

if name.lower() not in invited_dict.keys():
     print(f"Sorry {name} you aren't invited\n")
     answer = input("Do you want ask to admin list if you can be invited? Answer with (Y/N)\n")
     if answer.title() == 'Y':
          age = input("How old are you? \n")
          vehicle = input("How do you come at party for made a park reserv. \n")
          print("Let me add your at list...")
          no_invite_dict = {
               name : {
                    'age' : age,
                    'vehicle': vehicle,
                    }
          }
          no_invited_lts.append(no_invite_dict)
          for non_invited in no_invited_lts:
               print(non_invited)
     else:
          print("Ok you will loose the party's ")
else:
     print(f"{name} you're invited...")
    