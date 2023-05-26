
# First Method Using Third Variables
import time

x = input('Enter a Values in X : ')
y = input('Enter Second Values Y : ')
print(f'Before swap the variables x={x} ,y={y}',)


temp = x
x = y
y = temp
if time.sleep(2) == time.sleep(0):
    print(f'After swap the variables x={x} , y={y}')



