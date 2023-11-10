# 8.1 Message

def display_message():
    print("We are learning in this chapter how to work with functions.")

display_message()

# 8.2 Favorite Book

def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")

favorite_book("Harry Potter")

# 8.3 T-Shirt
def make_shirt(size, tshirt_quotes):
    print(f"\nSize of the T-Shirt: {size.title()}")
    print(f"Quote to print: {tshirt_quotes.title()}")

make_shirt('M', 'Hello World') 
make_shirt(size='S', tshirt_quotes='Have a good one.')

# 8.4 Large Shirts
def make_largue_tshirt(large_tshirt_quote, size="L"):
    print(f"\nSize of the T-Shirt: {size.title()}")
    print(f"Quote to print: {large_tshirt_quote}")

make_largue_tshirt(large_tshirt_quote="Welcome to USA")
