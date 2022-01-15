#20CS068
#Pruthvi Raj
# e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.


#defining function for finding commmon items
def findcommon(items):
    tracker = {}
    for item in items:
        if item not in tracker.keys():
            tracker[item] = 0
        tracker[item]+=1
    maxitem = None
    max = -1
    for key in tracker.keys():
        if((tracker[key]) > max):
            max = tracker[key]
            maxitem = key
    return maxitem,max

#declaring list and tuple
l1 = [1,2,3,2,3,2,4,5,6]
tuple1 = ("Orange","apple","Orange","mango")

#printing results
print(findcommon(l1))
#printing results
print(findcommon(tuple1))