# Question_1: Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# • Print the message, The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# • Print the message, Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
# • Print the message, The last three items in the list are:. Use a slice to print the last three items in the list.

print("\nAnswer")
Animals = ['Dog', 'cat', 'parrot', 'Cow', 'Horse', 'goat']
print(len(Animals)) # to know how many items are in the list

print('the first three items in the list are: ')
print(Animals[:3])

print('three items from the middle in the list are: ')
print(Animals[2:5])

print('the last three items in the list are: ')
print(Animals[-3:])



# Question_2: My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message, My favorite pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
 

print("\nAnswer")
My_Pizza = ['Neapolitan (Napoli)', 'Sicilian (Sfincione)', 'Margherita']
Friend_Pizza = My_Pizza[:]

My_Pizza.append('Chicken Tikka')

Friend_Pizza.append('Paneer Pizza')

print(f"\nMy favourite Pizza's are : ")
for pizza in My_Pizza:
    print(pizza)

print(f"\nMy Friends favourite Pizza's are : ")
for pizza in Friend_Pizza:
    print(pizza)






