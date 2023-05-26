print('Python List Comprehension')


string = ['hello','world']
upper_case = [i.upper() for i in string]
print(upper_case)



num = [i for i in range(10)]
print(num)



num_div = [i for i in range(20) if i %2 == 0]
print(num_div)