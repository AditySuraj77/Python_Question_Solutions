
print('Check Whether a String is Palindrome or Not')

user_string = input('Enter a Values : ')

reverse = user_string[::-1]

if user_string == reverse:
    print('Palindrome')
else:
    print('Not Palindrome')