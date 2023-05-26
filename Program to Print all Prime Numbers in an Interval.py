

lower = int(input('Enter a Lower Limit : '))
upper = int(input('Enter a Upper Limit : '))

print('Prime Numbers')
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                break

        else:
            print(num)