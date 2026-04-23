# Question_1: Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

print('\nAnswer')

profile = {
    'first_name':'sai',
    'last_name':'korumilli',
    'middle_name':'vamsi',
    'age':'24',
    'city':'bern'
    }

print(profile['first_name'].title())
print(profile['middle_name'].title())
print(profile['last_name'].title())
print(profile['age'])
print(profile['city'].title())

# Question_2: Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.


print('\nAnswer')
favourite_numbers = {
    'Sai':'17',
    'Ram':'4',
    'Siddu':'12',
    'Vishnu':'1',
    'Raj':'10'
}
print('The favourite number of Sai is : ' + favourite_numbers['Sai'] + '.')
print('The favourite number of Ram is : ' + favourite_numbers['Ram'] + '.')
print('The favourite number of Siddu is : ' + favourite_numbers['Siddu'] + '.')
print('The favourite number of Vishnu is : ' + favourite_numbers['Vishnu'] + '.')
print('The favourite number of Raj is : ' + favourite_numbers['Raj'] + '.')


# Question_3: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of three programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

glossary = {
    'print':'Prints out the output',
    'input':'Takes input from the user',
    'len()':'Gives the length of the list'
}
print('print :' + glossary['print'] + '.')
print('input :' + glossary['input'] + '.')
print('len() :' + glossary['len()'] + '.')