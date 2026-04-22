# Combine lists + loops + conditionals: filter a list of numbers, keeping only those divisible by 3 
divisible_by_3 = []
non_divisible_by_3 = []

for i in range(1,100):
    if i % 3 == 0:
        divisible_by_3.append(i)
    else:
        non_divisible_by_3.append(i)
print(f'The numbers whihc are divisible by 3 in the range(1,100) are : {divisible_by_3}')
print(f'there are {len(non_divisible_by_3)} numbers in the range (1,100) which are non divisible by 3')