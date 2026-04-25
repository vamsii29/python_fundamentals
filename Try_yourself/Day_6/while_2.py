# Question_1: Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

print('\nAnswer')
sandwich_orders = ['Chicken sandwich', 'Tuna sandwich', 'Paneer sandwich', 'Cheese sandwich', 'vegetable sandwich']
finished_sandwich = []
active = True

while active:
    progress = sandwich_orders.pop()
    print(f'Your {progress.title()} is in progress.')
    finished_sandwich.append(progress)
    if sandwich_orders == []:
        active = False

for sandwich in finished_sandwich:
    print(f'{sandwich.title()} is served.')

# Question_2: No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

print('\nAnswer')

sandwich_orders = ['Pastrami', 'Chicken sandwich', 'Tuna sandwich', 'Pastrami', 'Paneer sandwich', 'Pastrami',  'Cheese sandwich', 'vegetable sandwich', 'Pastrami']
finished_sandwich = []
active = True

while active:
    if sandwich_orders == []:
            active = False
    else:
        progress = sandwich_orders.pop()
        if progress.lower() == 'pastrami':
            print("We are sorry, we dont have Pastrami anymore.")
        else:
            print(f'Your {progress.title()} is in progress.')
            finished_sandwich.append(progress)
       

for sandwich in finished_sandwich:
    print(f'{sandwich.title()} is served.')



# Question_3: Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.

dream_vacation = {}

active = True
while active:
    print('\n')
    name = input('Please enter the name: ')
    place = input('If you could visit one place in the world where would you go? ')
    dream_vacation[name.title()] = place.title()
    poll = input("Do you want to take another poll? please enter 'yes' or 'no': ")
    if poll.lower() == 'no':
        active = False

for name, place in dream_vacation.items():
    print(f'The dream destination of {name} is : {place}')



