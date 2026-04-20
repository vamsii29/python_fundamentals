# Question_1: Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

print("Answer")
guests = ['harry', 'sam', 'Nelson', 'Abel']
for i in range(0,4):
    message = print(f"Hey {guests[i].title()}, I invite you to the Chirstmas Eve Party on this Saturday!!")



# Question_2: Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# • Start with your program from Question_1 Add a print statement at the end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.

print("Answer")
print(f"Unfortunately {guests[2].title()} is not available to make it to the Party")

guests[2] = 'Imran'

for i in range(0,4):
    message = print(f"Hey {guests[i].title()}, I invite you to the Chirstmas Eve Party on this Saturday!!")


# Question_3: More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement to the end of your program informing people that you found a bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

print("Answer")
print("I have managed to find a bigger table for our celebrations!!!")
guests.insert(0, 'Ram')
guests.insert(3, 'Krish')
guests.append('Kai')

for i in range(0,7):
    message = print(f"Hey {guests[i].title()}, I invite you to the Chirstmas Eve Party on this Saturday!!")




# Question_4: Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.


print("Answer")
print("I am sorry guys due to last minute changes I could only invite 2 people for the party")

for i in range (0,5):
    popped_guest = guests.pop()
    print(f"I am sorry {popped_guest}, i couldnt invite you to the party")


for i in range(0,2):
    print(f"Hey, {guests[i].title()} you are still invited to the party")
