#20CS068
#Pruthvi Raj
# d. Write a Python script to add a key to a dictionary.

#add key function
def addkey(dict,keyname,keyvalue):
    dict[keyname] = keyvalue
    return dict

#sample dictionary
dict = {0: 10, 1: 20}
keyname = 2
keyvalue = 30

dict = addkey(dict,keyname,keyvalue)
#printing dict
print(dict)