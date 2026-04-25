# Question_1: Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”

print('\nAnswer')
car = input('Please let us know which car you would like to rent: ')
print(f'Let me see if we can find a {car.title()} for you.')

# Question_2: Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message 
# saying they’ll have to wait for a table. Otherwise, report that their table is ready.

print('\nAnswer')
seats = int(input('Can we know how many people are here for the dinner today: '))
if seats > 8:
    print('I am sorry, you may have to wait until the tables are free.')
else:
    print("Your table is ready. Enjoy your meal!!!")


# Question_3: Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

print('\nAnswer')
num = int(input('Please enter a number you desire: '))
if num % 10 == 0:
    print(f'The {num} is a multiple of 10')
else:
    print(f'The {num} is not a multiple of 10')