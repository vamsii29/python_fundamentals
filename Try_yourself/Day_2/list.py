# Question_1: Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

name = ['Ramya', 'Vamsi', 'santosh', 'rajesh', 'abhinav', 'steve', 'ashok']

for i in range(0,7):
    print(name[i].title())

# Question_2: Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each mes-
# sage should be the same, but each message should be personalized with the person’s name.


for i in range(0,7):
    message = "Hi " + name[i].title() + " nice to meet you"
    print(message)

# Question_3: Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list 
# to print a series of statements about these items, such as “I would like to own a Honda motorcycle.

vehicles = ['Porsche 911', 'Bently continental GT', 'Harley Davidson fatboy', 'BMW S1000R']
print(f"I would like to own a {vehicles[1].title()} by 2027")
