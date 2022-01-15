#20CS068
#Pruthvi Raj
# c. Write a Python program to create an intersection, Union, difference of sets.


#declaring set1
set1 = {1,2,3,4,5}
#declaring set2
set2 = {3,4,5,6,7,8}

#printing union
print(set1.union(set2))
#printing req. queries
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))