#20CS068
#Pruthvi Raj
# c. Write a Python program to add an item in a tuple.


#creating a tuple
Pruthvi = (23, 43, 5, 87, 53)
print(Pruthvi)

#using merge of tuples with the + operator you can add an element and it will create a new tuple, because tuples are immutable
Pruthvi = Pruthvi + (94,)
print(Pruthvi)

#adding items in a specific index
Pruthvi = Pruthvi[:5] + (25, 2, 56) + Pruthvi[:5]
print(Pruthvi)

#converting the tuple to list
list1 = list(Pruthvi)

#use different ways to add items in list
list1.append(30)
Pruthvi = tuple(list1)
print(Pruthvi)