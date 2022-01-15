#20CS068
#Pruthvi Raj
# a. Write a Python program to add member(s) in a set and clear a set


#defining function to add items
def addtoset(set,items):
    for item in items:
        set.add(item)
    return set

#declaring set
set = {"1","2","3","4"}
#declaring list
items = ['a','b','c','d']
#calling function
set = addtoset(set,items)

#printing results
print(set)