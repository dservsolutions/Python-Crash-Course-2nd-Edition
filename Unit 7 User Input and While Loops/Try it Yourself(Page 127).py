# # 7.8 Deli
# sandwich_orders = ['chicken sandwich', 'egg sandwich', 'seafood sandwich', 
#                    'grilled cheese', 'pastrani', 'pastrani', 'pastrani']

# finished_sandwiches = []

# while sandwich_orders:
#     finished = sandwich_orders.pop()

#     print(f"I made your {finished.title()}")
#     finished_sandwiches.append(finished)
    
# print("\The followind Sandwiches are done.")
# for sandwiches in finished_sandwiches:
#     print(sandwiches.title())

# print(sandwich_orders)
# print(finished_sandwiches)

# # 7.9 No pastrani
# while 'pastrani' in finished_sandwiches:
#     finished_sandwiches.remove('pastrani')
#     print("Deli has run out of Pastrani")

# 7.10 Dream Vacation
# Setting a Flag
polling_active = True

while polling_active:
    data = {}
    name = input("\nPlease enter your name: ")
    place = input("\nIf you could visit one place in the word, where would you go? ")

    data[name] = place
    print(data.items())

     # Adding another
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() != 'yes':
        polling_active = False
    
    for name, place in data.items():
        print(f"{name.title()} like to went to {place}")

    



    