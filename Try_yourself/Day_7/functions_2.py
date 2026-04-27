# Question_1: T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

print('\nAnswer')

def make_shirt(size,message):
    '''This is to prepare a T-shirt'''
    print(f'The size of the shirt is {size} with a text "{message}" on the front.')

make_shirt('XL','Rapper')

make_shirt(size='L',message='BlackBerry')


# Question_2: Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

print('\nAnswer')

def make_shirt(message,size='L'):
    '''This is to prepare a T-shirt'''
    print(f'The size of the shirt is {size} with a text "{message}" on the front.')

make_shirt('I love python')
make_shirt('I love python', size='XL')

# Question_3: Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.

print('\nAnswer')
def describe_city(name,country='switzerland'):
    '''prints details fo the city'''
    print(f'{name.title()} is in {country.title()}')

describe_city('bern')
describe_city('basel')
describe_city('paris')
describe_city('paris','France')