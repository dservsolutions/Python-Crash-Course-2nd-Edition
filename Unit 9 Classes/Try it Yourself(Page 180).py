from restaurant import Restaurant
from privileges import Admin, Privileges

# 9.10 Imported Restaurant
# making an instance of restaurant

juice_palace = Restaurant('Palacio de los Jugos', 'Cuban cuisine')
juice_palace.describe_restaurant()


# 9.11 Imported Admin
admin = Privileges()

admin.show_privileges()