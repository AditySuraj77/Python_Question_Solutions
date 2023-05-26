print('Convert String to DateTime using')
from dateutil import parser

date_time = parser.parse('oct 4 2014 7:30PM ')

print(type(date_time))
print(date_time)