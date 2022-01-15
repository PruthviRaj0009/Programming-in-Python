#20CS068
#Pruthvi Raj
#  b. Write a Python script to merge two Python dictionaries.


# sample dictionaries
a1 = {'a': 900, 'b': 800}
a2 = {'c': 700, 'd': 600}
#making a copy of a1
b = a1.copy()
#adding a2 to b
b.update(a2)
#printing b
print(b)