while True:

    print('This Programmed check the number is Odd or Even')

    num = float(input('Enter a Number : '))

    if num % 2 == 0:
        print(num,'is Even Number')
    else:
        print(num,'is Odd Number')

    next = input('Do you Continue Programme y/n : ')
    if next == 'n':
        print('Programme End')
        break