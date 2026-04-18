# Question_1: Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
name = "Eric"
print(f"Hello {name}, would you like to learn some python today!!\n")


# Question_2: Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.

name = "korumilli Sai VaMsi"
print(f"this is the lowercase of the name {name.lower()}\n")
print(f"this is the uppercase of the name {name.upper()}\n")
print(f"this is the titlecase of the name {name.title()}\n")



# Question_3: Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:
#            Albert Einstein once said, “A person who never made a mistake never tried anything new.”

name = "Steve jobs"

print(f"{name.title()} once said, \"Your time is limited, so don't waste it living someone else's life.\"\n")

# Question_4: Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person. Then compose your message and store it in a new variable called message. Print your message.
famous_person = "steve jobs"
message = "Your time is limited, so don't waste it living someone else's life."

print(f"{famous_person.title()} once said, '{message}'")




# Question_5: Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

name = " 'Korumilli\tsai\tvamsi' "

print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())


