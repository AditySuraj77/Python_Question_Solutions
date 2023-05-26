print('Concatenate Two List Using Python')

# 1st.Method
''''
l1 = [1,2,3,45,'g','apple','orange']
l2 = [2,4,6,8,10,'fruit','Againfruits']

l3 =l1  + l2
print(l3)'''

# 2nd . Method
'''
l1 = [1,2,3,45,'g','apple','orange']
l2 = [2,4,6,8,10,'fruit','Againfruits']

new_list = list(set(l1+l2))
print(new_list)'''

#3rd . Method

l1 = [1,2,3,45,'g','apple','orange']
l2 = [2,4,6,8,10,'fruit','Againfruits']

l1.extend(l2)
print(l1)



