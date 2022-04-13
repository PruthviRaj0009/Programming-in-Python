'''
20CS068
Pruthvi Raj

Find Captain Room Number

Sample Input
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

Sample Output
8

Explanation: The list of room numbers contains 31 elements.
Since K is 5, there must be 6 groups of families. In the given list, all of the numbers
repeat 5 times except for room number 8.Hence, 8 is the Captain's room number.
'''

# taking integer input from user for number of reapeating family member in each family
K = int(input())
# taking list of integer input of numbers in families from user
lt = list(map(int, input().split()))[:(K+1)*K+1]
# creating two sets a & b
a = set()
b = set()

# for number in list of input lt:
for room in lt:
    # number not in a condition true then 
    if room not in a:
        # adding number to both of the sets
        a.add(room)
        b.add(room)
    # else condtition to pop/delete number from set b
    else:
        b.discard(room)
# changing set b to list b
b = list(b)
# printing b 
print(b)
