# Input Examples
# message = input("Tell me something and I will repeat it back to you: ")
# print(message)

# Writing Clear Prompts
# name = input("Please enter your name: ")
# print(f"\n Hello, {name}")

# Using int() to Accept Numerical Input
# age = input("How old are you?")
# print(age) 

# Rollercoaster
# height = input("How tall are you, in inches?")
# height = int(height)

# if height >= 48:
#     print("\n You're tall enough to ride ")
# else:
#     print("\n You'll be able to ride when you're a little older. ")

# Even or Odd Example
# number = int(input("Enter a number and I'll tell you if is even or odd: "))

# if number % 2 == 0:
#     print(f"The number {number} is Even")
# else:
#     print(f"The number {number} is Odd")


# Introducing While Loops
# The While Loop in Action
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# Letting the User Choose When to Quit
# prompt = "\nTell me something, and I'll repeat it back to you: "
# prompt += "\n Enten 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# Using a Flag
# active = True
# while active:
#     message = input(prompt)
    
#     if message == 'quit':
#         active = False
#     else:
#         print(message)


# Using break to Exit a Loop

# prompt = "\nPlease enter the name of a city that you have visited:"
# prompt += "\n(Enter 'quit' when you are finished. )"

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")


# Using continued in a Loop

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)


# Avoiding infinite loops
# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# Using a While Loop with List and Dictionaries.
# Start with users that need to be verified,
# and an empty list to hold confirmed users.

# unconfirmed_users = ['alice', 'brian', 'candance']
# confirmed_users = ['']

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# print(f"The following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# Removing All Instances of Specified Value from a list

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# Filling a Dictionary with User Input

responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nPlease enter your name: ")
    response = input("\n Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() != 'yes':
        polling_active = False

    # Polling is complete. Show the results.
    print("\n--- Poll results---")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")