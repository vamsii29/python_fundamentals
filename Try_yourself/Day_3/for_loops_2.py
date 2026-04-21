# Question_1: Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for num in range(1,21):
    print(num)

# Question_2: One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

for num in range(1,1000001):
    print(num)

# Question_3: Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

numbers = []
for num in range(1,1000001):
    numbers.append(num)

print(max(numbers))

print(min(numbers))

print(sum(numbers))

# Question_4: Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

for num in range(1,21,2):
    print(num)

# Question_5: Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

multiples_of_3 = [] 
# multiples_of_3 = [num*3 for num in range(1,11)] 

for num in range (1,11):
    multiples_of_3.append(num*3)

print(multiples_of_3)

# Question_6: Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

cubes = []
for num in range(1,11):
    cubes.append(num**3)

print(cubes)

# Question_7: Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cubes = [num**3 for num in range(1,11)]
print(cubes)