def create():
    data = input('Please enter your name and lastname: ')
    with open(file=f'{data.lower()}.d', mode='w') as file_object:
        content = file_object.write(data)


def read(file_name):
    with open(file_name, mode='r') as file:
        content = file.read()
        print(content)

def update(file_name):
    with open(file_name, mode='w') as file:
        new_data = input('Enter the new data to update: ')
        content = file.write(new_data)


# filename = 'david pedroso.d'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())
        
    
# # Make a List of Lines from a File
# with open(filename) as object:
#     lines = object.readlines()
#     for line in lines:
#         print(line)


# Working with a File's Contents
file = 'pi.txt'
with open(file) as new_file:
    lines = new_file.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))