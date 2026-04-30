# Question_1: Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a ValueError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the TypeError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number. 


# print('\nAnswer')
# try:
#     number_1 = input('Enter the first number you want to add: \n')
#     number_2 = input('Enter the second number you want to add: \n')
#     sum = int(number_1) + int(number_2)
# except ValueError:
#     print('Entered values should be a integer ')
# else:
#     print(sum)



# Question_2: Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.

# print('\nAnswer')
# while True:
#     try:
#         number_1 = input('Enter the first number you want to add \nEnter "q" to exit: ')
#         if number_1 == 'q':
#             break
#         number_2 = input('Enter the second number you want to add \nEnter "q" to exit: ')
#         if number_2 == 'q':
#             break
#         sum = int(number_1) + int(number_2)
#     except ValueError:
#         print('Entered values should be a integer only')
#     else:
#         print(f'The sum of the given numbers is {sum}')



# Question_3: Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
# names of cats in the first file and three names of dogs in the second file. Write
# a program that tries to read these files and print the contents of the file to the
# screen. Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing. Move one of the files to a dif-
# ferent location on your system, and make sure the code in the except block
# executes properly.


# print('\nAnswer')
# list = ['cats.txt', 'dogs.txt', 'humans.txt']
# for filename in list:
#     try:
#         with open(filename) as f_out:
#             lines = f_out.read()
#     except FileNotFoundError:
#         print('The file is missing!!!')
#     else:
#         print('The names are :')
#         print(f'{lines.title()}')




# Question_4: Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.

# print('\nAnswer')
# list = ['cats.txt', 'dogs.txt', 'humans.txt']
# for filename in list:
#     try:
#         with open(filename) as f_out:
#             lines = f_out.read()
#     except FileNotFoundError:
#         pass
#     else:
#         print('The names are :')
#         print(f'{lines.title()}')


# Question_5: Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
# and find a few texts you’d like to analyze. Download the text files for these
# works, or copy the raw text from your browser into a text file on your
# computer.
# You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the number
# of times 'row' appears in a string:
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# 3
# >>> line.lower().count('row')
# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for, regardless of how it’s
# formatted.
# Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text.


print('\nAnswer')
filename = 'gutenberg.txt'
try:
    with open(filename) as text:
        line = text.read()
except FileNotFoundError:
    pass
else:
    print(len(line))
    print(line.count('the'))





