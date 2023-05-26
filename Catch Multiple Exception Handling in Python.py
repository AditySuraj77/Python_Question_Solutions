print('Catch Multiple Exception Handling in Python')

string = input('Enter a Somethings : ')

try:
    num = int(input('Enter a values : '))
    print(string + num)
except (ValueError,TypeError) as a:
    print(a)
