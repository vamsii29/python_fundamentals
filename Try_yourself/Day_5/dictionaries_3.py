# Question_1: People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.



print('\nAnswer')

profile_1 = {
    'first_name':'sai',
    'last_name':'korumilli',
    'middle_name':'vamsi',
    'age':'24',
    'city':'bern'
    }

profile_2 = {
    'first_name':'Ramya',
    'last_name':'korumilli',
    'middle_name':'Sri',
    'age':'24',
    'city':'Paris'
    }

profile_3 = {
    'first_name':'sai',
    'last_name':'korumilli',
    'middle_name':'Teja',
    'age':'27',
    'city':'Rajahmundry'
    }

people = [profile_1, profile_2, profile_3]

for profile in people:
    print(profile)






# Question_2: Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.

print('\nAnswer')

max = {'kind':'dog', 'owner':'Teja'}
bolt = {'kind':'cat', 'owner':'Vamsi'}
harry = {'kind':'tortise', 'owner':'Raghu'}


pets = [max, bolt, harry]

for animals in pets:
    print(animals)


# Question_3: Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.



print('\nAnswer')
favourite_places = {
        'Ashok':['India', 'Australia'],
        'Bhavya':['Switzerland'],
        'Chiranjeevi':['Paris', 'Dubai', 'New york'],
        }
for name , place in favourite_places.items():
    if len(place) > 1:
        print('\nThe favourite places of ' + name.title() + ' are : ')
        for places in place:
            print(places.title())
    else:
        print('\nThe favourite place of ' + name.title() + ' is : ')
        for places in place:
            print(places.title())

    

# Question_3: Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

print('\nAnswer')

favourite_numbers = {
    'Sai': ['17', '6', '18', '45'],
    'Ram':['4', '8'],
    'Siddu':['24', '12', '15', '16'],
    'Vishnu':['1', '3', '9'],
    'Raj':['10']
    }

for name, num in favourite_numbers.items():
    if len(num) > 1:
        print("The favourite numbers of " + name.title() + " are: ")
        for nums in num:
            print(nums)
    else:
        print("The favourite number of " + name.title() + " is: ")
        for nums in num:
            print(nums)



# Question_4: Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the infor-
# mation you have stored about it.

print('\nAnswer')

cities = {
    'Bern':{'country':'Switzerland', 'population':'135,000', 'fact':'Old town is a UNESCO world heritage site'},
    'New York':{'country':'USA', 'population':'8.5 million', 'fact':'Home of Wall Street'},
    'Paris':{'country':'France', 'population':'2.1 million', 'fact':'City of Love'},
    'London':{'country':'UK', 'population':'9 million', 'fact':'One of the oldest underground rail system'}
    }

for city_name, city_info in cities.items():
    print(f"\n{city_name.title()}, a small info: ")
    print('The location is in : ' + city_info['country'] + '.')
    print('It has a population of : ' + city_info['population'] + '.' )
    print('A fact about this city is that : ' + city_info['fact'] + '.')


