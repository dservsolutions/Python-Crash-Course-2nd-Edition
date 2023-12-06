class User:
    def __init__(self, first_name, last_name, email):
        self.firstname = first_name
        self.lastname = last_name
        self.email = email
    # Method Describe User
    def describe_user(self):
        print(f"Name: {self.firstname.title()}\n")
        print(f"Lastname: {self.lastname.title()}\n")
        print(f"Email: {self.email}")
    # Method Greet User 
    def greet_user(self):
        print(f"Welcome {self.firstname}")