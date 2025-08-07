'''# Tuple is inmutable
tup1 = ('Mike',10,2.5)
tup2 = ('pop',1)
# print(tup1 + tup2)
# print(len(tup1))
tup1[0] = 0
print(tup1)
'''
# List is mutable
'''
numbers = [1,2,3,4,5]
numbers[0] = 0
print(numbers)'''

tup3 = (1,3,2,5,6,2,56,1)
tup_sort = sorted(tup3)
print(tup_sort)
print(tup3[3])