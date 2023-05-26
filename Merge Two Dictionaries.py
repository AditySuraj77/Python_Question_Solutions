print('Merge Two Dictionaries')


dict1 = {'Lisa':99,'Harman':70}
dict2 = {'Lisa':93,'Rohan':45}

print(dict1 | dict2)

# Using Update and copy()

dict3 = dict2.copy()

dict3.update(dict1)
print(dict3)