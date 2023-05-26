

print('Take Multiple Inputs from the User using Python')
'''
a,b,c = input('Enter a Three Value : ').split()

print(a)
print(b)
print(c)'''

# Take Multiple input from the user using list Comprehension

a,b,c = [int(x) for x in input('Enter a Value Here : ').split()]

print(a)
print(b)
print(c)