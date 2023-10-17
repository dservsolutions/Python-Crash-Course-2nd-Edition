# 3.4 Guess List
guess_list = ['maria','david', 'ale', 'yessie', 'amhari']
for names in guess_list:
    print(f'Dear {names.title()}, you are cordially invited to attend the dinner party we have planned')

# 3.5 Changing Guest List
# (a)
name = guess_list.pop(0)
print(f"{name.title()}, can't go to dinner")
# (b)
new_person = guess_list.append('jose')
print(guess_list)
# (c)
for new in guess_list:
    print(f'Dear {new.title()}, you are cordially invited to attend the dinner party we have planned')


# 3.6 More Guests
#(a)
for names in guess_list:
    print(f"Hello {names}, I've found a bigger dinner table")

#(b)
guess_list.insert(0, 'diana')
#(c)
guess_list.insert(3, 'jhonatan')
#(d)
guess_list.insert(-1, 'orestes')
print(guess_list)

# 3.7 Shrinking Guest List
for old_inv in guess_list:
    print(f"Hello {old_inv.title()}, Unfortunately the bigger tablet won't be arrive at time, and I only have space for two people. ")
#(b)
inv1 = guess_list.pop(0)
print(f"Dear {inv1.title()}, Sorry but I can't invite you at dinner")
inv2 = guess_list.pop(0)
print(f"Dear {inv2.title()}, Sorry but I can't invite you at dinner")
inv3 = guess_list.pop(0)
print(f"Dear {inv3.title()}, Sorry but I can't invite you at dinner")
inv4 = guess_list.pop(0)
print(f"Dear {inv4.title()}, Sorry but I can't invite you at dinner")
inv5 = guess_list.pop(0)
print(f"Dear {inv5.title()}, Sorry but I can't invite you at dinner")
inv6 = guess_list.pop(0)
print(f"Dear {inv6.title()}, Sorry but I can't invite you at dinner")
#(c)
for name in guess_list:
    print(f'{name.title()}, youre still invite to the dinner. ')
#(d)
del guess_list[0]
del guess_list[0]
print(guess_list)


