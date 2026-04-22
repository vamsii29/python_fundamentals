# Question_1: Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to each user:
# • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.

print('\nAnswer')
usernames = ['admin', 'vamsi', 'sai', 'sam', 'harry', 'eric']
for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report")
    else:
        print(f'Hello {user.title()}, thank you for logging in again!!!')


# Question_2: No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message is printed.


print('\nAnswer')
usernames = []
if usernames == []:
    print('We need to find User!!')
else:
    for user in usernames:
        if user == 'admin':
             print("Hello admin, would you like to see a status report")
        else:
             print(f'Hello {user.title()}, thank you for logging in again!!!')




# Question_3: Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. 
# • If a username has not been used, print a message saying that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.


print('\nAnswer')
current_users = ['agent007', 'mipaltan', 'vamsi', 'admin123', 'tissot', 'user']
new_users = ['AGENT007', 'User', 'phone', 'tim_cook', 'sai', 'Ramya']

for user in new_users:
    if user.lower() in current_users:
        print('Sorry, the username is taken, please try a new name')
    else:
        print(f'The username {user} is available!!!')
        current_users.append(user.lower())
    
# print(current_users)


# Question_4: Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# • Store the numbers 1 through 9 in a list.
# • Loop through the list.
# • Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th", and each result should be on a separate line.


print('\nAnswer')
numbers = range(1,10)
for num in numbers:
    if num == 1:
        print(f'{num} st \n')
    elif num == 2:
        print(f'{num} nd \n')
    elif num == 3:
        print(f'{num} rd \n')
    else:
        print(f'{num} th \n')