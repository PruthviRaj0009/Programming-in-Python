#20CS068
#Pruthvi Raj
# c. Write a Python program to sum all the items in a dictionary.

# funtction to find the sum of all vales of all keys in a dictionary
def sumofdict(dict):
    sum = 0
    #for every key add the value to sum
    for key in dict.keys():
        sum += dict[key]
    return sum

#sample dictionary
dict = {'A': 3, 'B':4, 'C':5}
#printing sumofdict
print(sumofdict(dict))