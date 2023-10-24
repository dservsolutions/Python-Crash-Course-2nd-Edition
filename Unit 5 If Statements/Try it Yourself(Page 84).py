# Alien Color 1
alien_color = ['green', 'yellow', 'red']
# (a)
if 'green' in alien_color:
    print("You just earned 5 pts. ")

# (b)
color = 'black'
if color in alien_color:
    print("These color is in the list")
if color is not alien_color:
    print("NO")
    
# 5.4 Aliens Color 2
#(a)
if 'green' in alien_color:
    print("Your earned 5 pts.")
else:
    print("Your earned 10 pts. ")

#(c)
print("Select a option below: ")
color = 'black'
if color == 'black':
    print("Ok, you earned 10 pts")

if color == 'blue':
    print("You earned 15 pts")
else:
    if color == 'black':
        print("Your earned 10 pts")
