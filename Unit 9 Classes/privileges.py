from users import User

class Privileges:
        def __init__(self):
             self.privileges_list = ["can add post", "can delete post", "can ban user"]

    # Method that show the user privileges.
        def show_privileges(self):
             print("Has the followings privileges:")
             for privilege in self.privileges_list:
                print(privilege.title())

# 9.7 Admin
class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.pri = Privileges()
        
    # Making an instance
admin = Admin('david', 'pedroso', 'ppdavisito89@outlook.es')