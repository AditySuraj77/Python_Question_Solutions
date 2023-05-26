
print('Read a File Line by Line Into a List?')
'''
f = open('new.txt','r')

lines= f.readlines()
print(lines)

new_lines = [x.strip() for x in lines]
print(new_lines)'''

# Using for loop and list comprehension

f = open('new.txt','r')

lines = [line for line in f]

new_line = [x.strip() for x in lines]
print(new_line)