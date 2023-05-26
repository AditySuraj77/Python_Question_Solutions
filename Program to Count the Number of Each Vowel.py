
print('Program to Count the Number of Each Vowel')

a = input('Enter a SomeThings : ')

vowels = 'aeiou'

a = a.casefold()
print(a)

count = {}.fromkeys(vowels,0)

for char in a:
    if char in count:
        count[char] +=1
print(count)