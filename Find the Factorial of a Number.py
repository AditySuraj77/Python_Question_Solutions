
# Using For loop to find given number of factorial

num = int(input('Enter a Number : '))

fact = 1
if num < 0:
    print('Factorial 0 is does not exists')
if num == 0:
    print('Factorial is = ',1)
if num > 0:
    for i in range(1,num+1):
        fact = fact * i
print('The Factorial of given number is = ',fact)