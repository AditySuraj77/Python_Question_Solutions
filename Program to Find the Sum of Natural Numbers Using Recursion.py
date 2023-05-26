
print('Program to Find the Sum of Natural Numbers Using Recursion')

def NNS(n):
    if n <=1:
        return n
    else:
        return (n) + NNS(n-1)

user_num = int(input('Enter a Number here : '))
print('The sum of Natural umber is = ', NNS(user_num))