# Question_1: Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.
print('\nAnswer')


prompt = ("Please enter the toppings you want to add to your pizza:  \nenter 'quit' to complete the customization.\n" )
pizza_toppings = input(prompt)
while pizza_toppings != 'quit':
    print(f'{pizza_toppings} are added to your pizza!!!!\n')
    if pizza_toppings != 'quit':
        pizza_toppings = input(prompt)
    
print("your Pizza is ready !!!!!")
        

# Question_2: Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
print('\nAnswer')


age = (input("what is your age in years: \nenter quit to exit.\n"))

while age != 'quit':
    if int(age) < 3:
        print('The ticket is free')
        
    elif int(age) <= 12:
        print('The ticket price is 10$')
    
    elif int(age) > 12:
        print('The ticket price is 15$')
    
    age = (input("what is your age in years: \nenter quit to exit.\n"))

       

# Question_3: Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# • Use a break statement to exit the loop when the user enters a 'quit' value.
print('\nAnswer')

age = (input("what is your age in years: \nenter quit to exit.\n"))

while True:
    if age == 'quit': # if this condition is at the last there might be a value error while running the elif commands as age is not a integer when the value is 'quit'
        break
    elif int(age) < 3:
        print('The ticket is free')
        
    elif int(age) <= 12:
        print('The ticket price is 10$')
    
    elif int(age) > 12:
        print('The ticket price is 15$')
    
    age = (input("what is your age in years: \nenter quit to exit.\n"))


# Question_4: Infinity: Write a loop that never ends, and run it. (To end the loop, press
# ctrl-C or close the window displaying the output.)

print('\nAnswer')
click = input("Type 'start' to start the infinte loop and 'quit' to exit: ")
if click.lower() == 'start':
    while True:
        print('This is a infinte loop, press ctrl + C to exit')
elif click.lower() == 'quit':
    print("Program exited!!!")