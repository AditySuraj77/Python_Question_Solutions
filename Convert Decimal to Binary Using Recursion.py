print('Convert Decimal to Binary Using Recursion')

def ConvertBinary(n):
    if n> 1:
        ConvertBinary(n//2)
    print(n%2,end=" ")
ConvertBinary(10)