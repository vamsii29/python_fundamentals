# Write a program: grade classifier — takes a score (0–100), prints the letter grade with a message

try: 
    score = int(input("What is your score out of 100: "))
except ValueError:
     score = int(input("Please enter a integer from 0 to 100 "))
if score > 100:
    print('Please check your score and try again!!!')
elif score < 40:
    print("Fail")
elif score < 60:
    print("Grade E")
elif score < 70:
    print("Grade D")
elif score < 80:
    print("Grade C")
elif score < 90:
    print("Grade B")
elif score <= 100:
    print("Grade A")



