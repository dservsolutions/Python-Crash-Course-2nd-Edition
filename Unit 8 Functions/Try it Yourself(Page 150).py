from defining_a_function import build_profile

# 8.12 Sandwiches
# def make_order(*menu_items):
#     print("A sandwich with the following menu have been ordered. ")
#     for menu in menu_items:
#         print(f"-{menu}")
        

# make_order('steak')
# make_order('steak', 'cheese', 'bacon')
# make_order('steak', 'meet', 'cheese')


# 8.13
# dserv = build_profile('dserv', 'llc', location='Miami, FL', country='USA')
# print(dserv)

# 8.14
def make_car(manufacturer, model, **carinfo):
    carinfo['manufacturer'] = manufacturer
    carinfo['model'] = model
    return carinfo

car = make_car('lada', 2107, color='white', year=1976)
print(car)


