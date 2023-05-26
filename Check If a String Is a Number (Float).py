print(' Check If a String Is a Number (Float)')

num = input('Enter SomeThings : ')

def check_float(num):
    try:
        float(num)
        return True
    except:
        return False

print(check_float(num))