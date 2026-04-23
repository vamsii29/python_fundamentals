# Question_1: Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

print('\nAnswer')
glossary = {
    'print':'Prints out the output',
    'input':'Takes input from the user',
    'len()':'Gives the length of the list',
    'variable':'A named referance to a value stored in memory',
    'loop':'A control structure that repeats a block of code multiple times',
    'Tuple':'An ordered,immmutable collection of items, Once created cannot be changed',
    'List':'An ordered, mutable collection of items',
    'function':'A reusable blocl of code designed to perform specific tasks'
}
for words in glossary.keys():
    print(f'{words} : {glossary[words]}')


# Question_2: Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.


print('\nAnswer')
Rivers = {
    'ganga':'india',
    'nile':'egypt',
    'amazon':'south america'
}
for river in Rivers.keys():
    print(f'The river {river.title()} runs through {Rivers[river].title()}')

print("\nThe rivers included in the dictionary are : ")
for river in Rivers.keys():
    print(river.title())


print("\nThe countries included in the dictionary are : ")
for country in Rivers.values():
    print(country.title())


# Question_3: Polling: Use the code in favorite_languages.py (page 104).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

print('\nAnswer')
fav_languages = {
    'Aman':'C',
    'Billa':'Rust',
    'Charan':'Go',
    'Deepak':'Python',
    'Eswar':'Java',
    'Fredrick':'Rust',
    'Ganga':'C++',
    'Harsh':'Go',
}

people_to_poll = ['Vamsi','Suraj','Ganga','Aman','Ram']

for people in people_to_poll:
    if people in fav_languages.keys():
        print("Thank you " + str(people.title()) + " for participating in the poll!!")
    else:
        print("Hi " + str(people.title()) + " we invite you to participate in this poll!!!!" )


