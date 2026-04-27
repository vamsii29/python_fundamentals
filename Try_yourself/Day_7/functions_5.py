# Question_1: Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sand-
# wich that is being ordered. Call the function three times, using a different num-
# ber of arguments each time.
print('\nAnswer')
def items_on_sandwich(*items):
    print('The sandwich has : ')
    for item in items:
        print(item)

items_on_sandwich('onions', 'chicken', 'olives', 'eggs')


# Question_2: User Profile: Start with a copy of user_profile.py from page 153. Build
# a profile of yourself by calling build_profile(), using your first and last names
# and three other key-value pairs that describe you.


print('\nAnswer')

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('vamsi','korumilli', age = '24', edu = 'MSc in compute science', field = 'cs')
print(user_profile)

# Question_3: Cars: Write a function that stores information about a car in a diction-
# ary. The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the func-
# tion with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly

def make_cars(manufacture_details, model_details, **car_info):
    car = {}
    car['manufacture'] = manufacture_details
    car['model'] = model_details
    for keys,value in car_info.items():
        car[keys] = value
    return car

car = make_cars('porsche', '911', color = 'gun metal grey', gearbox = 'manual')
print(car)
