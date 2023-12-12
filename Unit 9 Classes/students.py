class Students:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # Method student info
    def students_inf(self):
        print(f"Full Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        
# Making a instance
# std_1 = Students('David', 'Pedroso', 33)


# std_1.students_inf()