# Question_1: Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.

print('\nAnswer')
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'The name of the restaurant is {self.restaurant_name.title()} and it is a {self.cuisine_type.title()} restaurant')

    def open_restaurant(self):
        print(f'The {self.restaurant_name.title()} restaurant is now open.')


my_restaurant = Restaurant('Paradise', 'Indian')

print(f'Name : {my_restaurant.restaurant_name.title()}')
print(f'Cuisine : {my_restaurant.cuisine_type.title()}')


my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()




# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

print('\nAnswer')

restaurant_1 = Restaurant('MeFill', 'Andhra')
restaurant_2 = Restaurant('Udupi', 'Tamil')
restaurant_3 = Restaurant('Burger King', 'American')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()


# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.


print('\nAnswer')
class User():
    def __init__(self, first_name, last_name, *user_profile):
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile = user_profile

    def describe_user(self):
        print(f'Here are the details of the User : {self.first_name.title()} {self.last_name.title()}')
        print(f'Additional information: {self.user_profile}')
    
    def greet_user(self):
        print(f'Hello {self.last_name.title()}, Hope you are doing good!!')


user_1 = User('sai','korumilli')
user_2 = User('Ramya','Anumolu', '23', 'India')
        
user_1.describe_user()
user_2.describe_user()

user_1.greet_user()
user_2.greet_user()