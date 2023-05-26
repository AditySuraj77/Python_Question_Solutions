
print('Check if Nuber is Prime are Not')

num = int(input('Enter a Number : '))

if num == 1:
    print('it is not Prime')
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print('It i not Prime')
    else:
        print('Prime Number')