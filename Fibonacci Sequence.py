
while True:

    print('Fibonacci Sequence')

    a = 0
    b = 1

    num = int(input('Enter a Number : '))

    if num == 1:
        print(a)
    else:
        for i in range(2,num):
            c = a + b
            a = b
            b = a
            print(c)