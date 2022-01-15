#20CS068
#Pruthvi Raj
# b. Write a Python program to remove an item from a set if it is present in the set.


#defining function to remove items
def removeitem(set,item):
    set.discard(item)
    return set
    
#declaring set
set = {1,2,3,4,5,6,7}
#calling function
set = removeitem(set,2)
#printing results
print(set)
#calling function
set = removeitem(set,10)
#printing results
print(set)