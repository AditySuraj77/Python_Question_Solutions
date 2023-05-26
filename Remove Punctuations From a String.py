print('Remove Punctuations From a String ')

punc = '''!()-[]{};:'"\,<>./~_^$&%#@*?'''

string = input('Enter a Some Things : ')

empty_string = ""

for i in string:
    if i not in punc:
        empty_string = empty_string + i
print(empty_string)