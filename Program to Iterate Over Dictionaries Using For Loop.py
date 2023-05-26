print('Program to Iterate Over Dictionaries Using For Loop')




test_team = {'Player_1':'Rohit Sharma', 'Player_2':'Shubman Gill', 'Player_3':'Cheteshwar Pujara', 'Player_4':'Virat Kohli',
 'Player_5':'Ajinkya Rahane', 'Player_6':'KS Bharat'}

for key,value in test_team.items():
 print(key,'-',value)

for key in test_team:
 print(key)

for value in test_team.values():
 print(value)