# Question_1: Imported Restaurant: Using your latest Restaurant class, store it in a mod-
# ule. Make a separate file that imports Restaurant. Make a Restaurant instance,
# and call one of Restaurant’s methods to show that the import statement is work-
# ing properly.


from class_3 import Restaurant, Ice_cream 

my_restaurant = Ice_cream('Paradise', 'Indian')
my_restaurant.display_flavours()




# Question_2: Imported Admin: Start with your work from Exercise 9-8 (page 178).
# Store the classes User, Privileges, and Admin in one module. Create a sepa-
# rate file, make an Admin instance, and call show_privileges() to show that
# everything is working correctly.

from imported_admin import Admin

user_1 = Admin('sai','korumilli')
user_1.privilage_instance.show_privilages()
