# Question_1: Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.
print('\nAnswer')
filename = 'guest.txt'
with open(filename ,'a') as guest_name:
    name = input('Enter the name of the guest: ')
    guest_name.write(f'The name of the guest is {name.title()} \n')
    



# Question_2: Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.
print('\nAnswer')
filename_2 = 'guest_book.txt'

with open(filename_2, 'w') as guest_visiting:
    while True:
        name = input('Enter the guest name \nEnter "q" to exit: ')
        if name == 'q':
            break
        else:
            print(f'welcome {name},hope you enjoy your trip')
            guest_visiting.write(f'The guest named {name.title()} is present at the trip \n')






# Question_3: Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.
print('\nAnswer')
filename_3 = 'reasons.txt'

with open(filename_3,'a') as reasons:
    while True:
        ask_for_reason = input('Why do you like programming \nEnter "q" to exit: ')
        if ask_for_reason == 'q':
            break
        else:
            reasons.write(f'{ask_for_reason} \n')