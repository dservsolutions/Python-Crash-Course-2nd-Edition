# 5.1 Conditional Test
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 5.2 More conditional test
guess_list = ['jhon', 'mari', 'jose', 'david']
new_invited=  'david'

# (a)
if new_invited not in guess_list:
    print(f"{new_invited.title()}, is not invited.")
else:
    print(f'{new_invited.title()}, is in the invited list.')

# (b)
if new_invited.title() == new_invited.lower():
    print(f"{new_invited}")
else:
    print("They are not the same")

# (c)
david = 34
karen = 26
if david == karen:
    print("They have the same age")
elif david != karen:
    print("They don't have the same age. ")

if david > karen:
    print("David is most older.")
else:
    print("Karen is most older.")


if david and karen == 30:
    print('They have 30 years old')
else:
    print("They don't have 30 years old")


if david or karen >= 30:
    print("One of the them have more than 30 years old")
else:
    print("No one of them have 30 years old")


names = ['david', 'diana']
other = 'jhon'

if other in names:
    print(f"{other.title()}, is in the list")
else:
    print(f"{other.title()}, is not in the list")









