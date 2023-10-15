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
