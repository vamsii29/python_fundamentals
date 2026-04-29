# Question_1: Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. Print the number of customers the
# restaurant has served.
# Then change this value and print it again. Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any num-
# ber you like that could represent how many customers were served in, say, a
# day of business.
print('\nAnswer')
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'The name of the restaurant is {self.restaurant_name.title()} and it is a {self.cuisine_type.title()} restaurant')

    def open_restaurant(self):
        print(f'The {self.restaurant_name.title()} restaurant is now open.')
    
    def set_number_served(self,number):
        self.number_served = number
        print(f'The {self.restaurant_name} restaurant has served {self.number_served}')
    
    def increment_number_served(self, customers):
        self.number_served += customers


my_restaurant = Restaurant('Paradise', 'Indian')


print(f'Name : {my_restaurant.restaurant_name.title()}')
print(f'Cuisine : {my_restaurant.cuisine_type.title()}')


print(f'The numbers served by the restaurant till now are {my_restaurant.number_served}')
my_restaurant.set_number_served(5)
my_restaurant.increment_number_served(10)

print(my_restaurant.number_served)




# Question_2: Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

print('\nAnswer')
class User():
    def __init__(self, first_name, last_name, *user_profile):
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile = user_profile
        self.login_attempts = 0

    def describe_user(self):
        print(f'Here are the details of the User : {self.first_name.title()} {self.last_name.title()}')
        print(f'Additional information: {self.user_profile}')
    
    def greet_user(self):
        print(f'Hello {self.last_name.title()}, Hope you are doing good!!')

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User('sai','korumilli')
user_2 = User('Ramya','Anumolu', '23', 'India')
        
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)