print('Program to Find Numbers Divisible by Another Number')

l = [39,45,33,13,67,39,49]

result = list(filter(lambda x : x % 13 == 0, l))
print(result)


for num in l:
    if num%13 == 0:
        print(num)