# Question_1: Printing Models: Put the functions for the example print_models.py in a
# separate file called printing_functions.py. Write an import statement at the top
# of print_models.py, and modify the file to use the imported functions.

# print('\nAnswer')
# import printing_functions as p

# p.display_message()



# Question_2: Imports: Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *


# import printing_functions as pf
# pf.display_message()

# from printing_functions import display_message
# display_message()


# from printing_functions import make_shirt as ms
# ms('XL', 'This function is imported')


from printing_functions import *
make_shirt('L','This is nice')