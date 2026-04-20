# Question_1: Seeing the World: Think of at least five places in the world you’d like to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.

places_to_visit = ['Swiss Alps', 'Lindt Chocolate Factory', 'Louvre Museum', 'Taj Mahal', 'Eiffel tower']

# • Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.

print('1')
print(places_to_visit)

# • Use sorted() to print your list in alphabetical order without modifying the actual list.

print('2')
print(sorted(places_to_visit))

# • Show that your list is still in its original order by printing it.

print('3')
print(places_to_visit)

# • Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

print('4')
print(sorted(places_to_visit, reverse=True))

# • Show that your list is still in its original order by printing it again.

print('5')
print(places_to_visit)

# • Use reverse() to change the order of your list. Print the list to show that its order has changed.

print('6')
places_to_visit.reverse()
print(places_to_visit)


# • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

print('7')
places_to_visit.reverse()
print(places_to_visit)

# • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

print('8')
places_to_visit.sort()
print(places_to_visit)

# • Use sort() to change your list so it’s stored in reverse alphabetical order.


print('9')
places_to_visit.sort(reverse=True)
print(places_to_visit)


# Print the list to show that its order has changed.

print('10')
print(places_to_visit)




# Question_2: Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner.


print("Answer")
guests = ['harry', 'sam', 'Nelson', 'Abel']

print(f"I am inviting {len(guests)} members for the party") 




# Question_3: Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or any-
# thing else you’d like. Write a program that creates a list containing these item and then uses each function introduced in this chapter at least once.


# mountains = ['Mount Fujji', 'Mount Everest']
# rivers = ['Ganga', 'Godavari']
# Countries = ['India', 'Switzerland']
# Cities = ['Zurich', 'Bern']

Languages = ['Telugu', 'English', 'German', 'French', 'Italian']

print(Languages[2]) # Accessing elements from a list

print(f"{Languages[0]} is my mother toungue") # Using individual values from the lists

Languages[1] = 'Tamil'
print(Languages) # Modifing elements in the list 

Languages.append('Spanish') 
print(Languages) # adding elements to the end of the list

Languages.insert(2, 'Urdu')
print(Languages) # inserting elements to the list 

del Languages[0]
print(Languages) # deleting elements of the list

popped = Languages.pop(2)
print(popped) # removing the last element of the list
print(Languages)

Languages.remove('French')
print(Languages) # removing items using value










