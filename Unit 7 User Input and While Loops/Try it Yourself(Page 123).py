# 7.4 Pizza Toppings
# prompt = "\nEnter a series of Pizza Toppings"
# prompt += "\nPlease enter 'quit' for stop the program."
# message = ""

# while message != 'quit':
#     message  = input(prompt)
#     print(message)

# 7.5 Movie Tickets
# age = int(input("How old are you?\n"))

# while age < 3:
#     print("Your ticket is free...")
#     break
# else:
#     if (age > 3 ) and (age <= 12 ):
#         print("The ticket price is $12.")
#     else:
#         print("Your ticket cost $15.")

# 7.6 Three Exits
# active = True

# while active == True:
#     name = input("Please enter your username: \n")
#     if name == 'admin':
#         print("Welcome Admin")
#         active = False
#     else:
#         name += name

# Another Example with break:

# question = "Please enter a verb: \n"
# question += "Write 'quit' to close the program. \n"

# while question != "quit":
#     message = input(question)

#     if message.lower() == "quit":
#         break

# 7.7 Infinity
infinity = int(input("Write a number more than 0, please: \n"))

while infinity > 0:
    print("Hello World.....\n")