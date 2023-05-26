
print('Programmed Check Leap Year')

year = int(input('Enter a Year : '))

if (year% 400 == 0) and (year% 100 == 0):
    print(year,'Leap Year')
elif (year % 4 == 0) and (year % 100 != 0):
    print(year,'is Leap year')
else:
    print(year,'Is Not Leap Year')