# Question_1: Magicians: Make a list of magician’s names. Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list.
print('\nAnswer')
def show_magicians(name):
    '''printing out the names of the magicians!!!'''
    for names in name:
        print(f'{names.title()}')

magicians = ['sai', 'vamsi', 'ramya', 'charan']
show_magicians(magicians)



# Question_2: Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by add-
# ing the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.
# print('\nAnswer')

# greatname = []
# def make_great(name, greatname):
#     while name != []:
#         names = name.pop()
#         great_magician = 'great' + ' ' + names
#         greatname.append(great_magician)



# make_great(magicians,greatname)
# show_magicians(greatname)



# Question_3: Unchanged Magicians: Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the origi-
# nal names and one list with the Great added to each magician’s name.

print('\nAnswer')


greatname = []
def make_great(name, greatname):
    while name != []:
        names = name.pop()
        great_magician = 'great' + ' ' + names
        greatname.append(great_magician)

make_great(magicians[:],greatname)
show_magicians(magicians)
show_magicians(greatname)