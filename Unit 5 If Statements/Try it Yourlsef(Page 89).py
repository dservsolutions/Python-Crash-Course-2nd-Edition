# 5.8 Hello admin
# usernames= ['admin', 'invited', 'jhoan', 'jose', 'mary']

# for users in usernames:
#     if 'admin' in users:
#         print(f"Hello {users}, would you like to see a special report")
#     else:
#         print(f"Hello {users}, thanks you for loggin.")

# 5.9 No users
# if usernames == []:
#     print("We need to find some users")
# else:
#     print("We have users")

# 5.10 Checking usernames
# (a)
# current_users = ['pepe', 'juan', 'pedro', 'Jhon', 'admin']
# # (b)
# new_users = ['david', 'valeria', 'paulo', 'jHON', 'admin']
# new_users_formated = new_users[:]

# # (c)
# for user in new_users_formated:
#     if user.title() in current_users:
#         print(f"Choose another user because {user} is in use ")
#     else:
#         print("Username is available")

# 5.11 Ordinal Numbers
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for num in numbers:
    if '1' in num:
        print(f"{num}st")
    elif '2' in num:
        print(f"{num}nd")
    elif '3' in num:
        print(f"{num}rd")
    else:
        print(f"{num}st")