print('Program to Check if a Key is Already Present in a Dictionary')

rcb_team = {'FAF':'C','Maxwell':'B','Virat':'B','Dinesh':'W-B','Rawat':'W-B','Mahipal':'B','Siraj':'Bow'}

inpu_user = input('Enter a Key : ')

if inpu_user in rcb_team.keys():
    print('its is Present')
else:
    print('Not Present')