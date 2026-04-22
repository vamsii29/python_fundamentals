# Question_1: 
# Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. 

Pet = 'Dog'
print("Is Pet == 'Dog'?, I predict True")
print(Pet == 'Dog')

print("Is Pet == 'Cat'?, I predit False")
print(Pet == 'Cat')


# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.

print("\nAnswer")
car = ['Audi', 'BMW', 'Porsche', 'Bently', 'Jaguar', 'Ferrari']
print('Audi' in car) # True
print('Bmw' in car) # False
print('BMW' in car) # True
print('audi' in car) # False
print('Tesla' in car and 'Porsche' in car) # False
print('Pizza' in car) # False
print('Audi' in car or 'bently' in car) # True
print('Audi' in car and 'Ferrari' in car) # True
print('Burger' in car or 'BMW' in car) # True



# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# • Tests for equality and inequality with strings

print("\nAnswer")
print(1>3) # False
print(3>2) # True

# • Tests using the lower() function

print("\nAnswer")
print(Pet.lower() == 'dog') # True
print(Pet.upper() == 'Dog') # False


# • Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to

print("\nAnswer")
print((1+2) >= 3) # True
print((999-215) < 1) # False

# • Tests using the and keyword and the or keyword

print("\nAnswer")
print('Tesla' in car and 'BMW' in car) # False
print('BMW' in car or 'Porsche' in car ) # True


# • Test whether an item is in a list

print("\nAnswer")
print('Audi' in car) # True


# • Test whether an item is not in a list

print("\nAnswer")
print("Jeep" in car) #False