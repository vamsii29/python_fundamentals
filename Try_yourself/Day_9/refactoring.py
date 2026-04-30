# Question_1: Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dump() to store this number in a file. Write a separate pro-
# gram that reads in this value and prints the message, “I know your favorite
# number! It’s _____.
# ”


import json

# print('\nAnswer')
# filename= 'fav_number.json'
# try:
#     with open(filename, 'w') as fav_input:
#         number = input('input your favourite number: ')
#         json.dump(number, fav_input)
# except FileNotFoundError:
#     pass
# else:
#     with open(filename) as fav_output:
#         answer = json.load(fav_output)
#         print(f'I know your favourite number: {answer}')




# Question_2: Favorite Number Remembered: Combine the two programs from
# Exercise 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store it in a
# file. Run the program twice to see that it works.

# print('\nAnswer')

# filename= 'fav_number.json'
# try:
#     with open(filename) as fav_input:
#         answer = json.load(fav_input)
# except FileNotFoundError:
#     with open(filename, 'w') as fav_output:
#         number = input('input your favourite number: ')
#         json.dump(number, fav_output)
#         print('Your favourite number is registered!!!')
# else:    
#     print(f'I know your favourite number: {answer}')






# Question_3: Verify User: The final listing for remember_me.py assumes either that the
# user has already entered their username or that the program is running for the
# first time. We should modify it in case the current user is not the person who
# last used the program.
# Before printing a welcome back message in greet_user(), ask the user if
# this is the correct username. If it’s not, call get_new_username() to get the correct
# username

print('\nAnswer')
filename = 'username.json'


def get_username():
    with open(filename, 'w') as user:
        username = input('Enter your username: ')
        json.dump(username, user)
        return username

def verify_username():
    with open(filename) as user:
        username = json.load(user)
    print(f'Please verify your username: {username}')
    verify = input('Enter "y" is correct and "n" if incorrect: ')
    if verify == 'n':
        username = get_username()
    return username

def main():
    try:
        answer = verify_username()
    except FileNotFoundError:
        get_username()
    else:
        print(f'welcome back {answer}')


main()