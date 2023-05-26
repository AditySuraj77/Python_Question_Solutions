
while True:


    print('~~~~~~~~~~~Calculator~~~~~~~~~~~')

    num1 = float(input('Enter a First Number : '))
    num2 = float(input('Enter a Second Number : '))

    print('Choice Operation + - * / ')

    choice = input('Enter a Operation : ')

    if choice == '+':
        print('The Addition of Given Number = ',num1 + num2)
    elif choice == '-':
        print('The Subtraction of Given Number = ',num1 - num2)
    elif choice == '*':
        print('The Multiplication of Given Number = ',num1 * num2)
    elif choice == '/':
        print('The Division of Given Number = ',num1 / num2)
    else:
        print('Invalid Input')

    next = input('Do You continue calculation y/n : ')

    if next == 'n':
        print('Programmed End')
        break