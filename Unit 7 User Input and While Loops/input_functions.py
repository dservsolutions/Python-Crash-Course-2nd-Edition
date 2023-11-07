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
x = 1
while x <= 5:
    print(x)
    x += 1