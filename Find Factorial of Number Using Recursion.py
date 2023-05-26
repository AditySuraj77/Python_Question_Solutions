print('Find Factorial of Number Using Recursion')

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

n = int(input('Enter Number Here : '))

if n <=0:
    print("Factorial does't exists")
else:
    print(f'The Factorial of {n} number is = ',fact(n))