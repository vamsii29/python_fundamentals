# Question_1: Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.

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

class Ice_cream(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['Chocolate', 'Strawberry', 'Blueberry']
    
    def display_flavours(self):
        for flavours in self.flavours:
            print(flavours)





my_restaurant = Ice_cream('Paradise', 'Indian')

my_restaurant.display_flavours()







# Question_2: Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

# Question_3: Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.


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


class Privileges():
    def __init__(self, privilages = ['can add post', 'can delete post', 'can ban user']):
        self.privilages = privilages
        
    def show_privilages(self):
        for privilages in self.privilages:
            print(privilages)


class Admin(User):

    def __init__(self, first_name, last_name, *user_profile):
        super().__init__(first_name, last_name, *user_profile)
        self.privilage_instance = Privileges()
        
    
    # def show_privilages(self):
    #     for privilages in self.privilages:
    #         print(privilages)



user_1 = Admin('sai','korumilli')

user_1.privilage_instance.show_privilages()



# Question_4: Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the car’s range.

print('\nAnswer')
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
        


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """ Initialize attributes of the parent class.Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()



my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()