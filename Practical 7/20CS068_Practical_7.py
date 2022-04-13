'''
20CS068
Pruthvi Raj

Lapindrome is defined as a string which when split in the middle, gives two
halves having the same characters and same frequency of each character. If there
are odd number of characters in the string, we ignore the middle character and
check for lapindrome. For example gaga is a lapindrome, since the two halves ga
and ga have the same characters with same frequency. Also, abccab, rotor and
xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome.
The two halves contain the same characters but their frequencies do not match.
Your task is simple. Given a string, you need to tell if it is a lapindrome.

Input:
6
gaga
abcde
rotor
xyzxy
abbaab
ababc

Output:
YES
NO
YES
YES
NO
NO
'''

# taking input from user for testcases
testcases = int(input())
# for loop until  test cases
for i in range(testcases):
    # Taking input word as list
    lst = list(input())
    # splitting lst into two halves
    split = len(lst) // 2
    lst1 = lst[:split]
    # condition
    if len(lst) % 2 == 0:
        lst2 = lst[split:]
        # if length of word is odd, ignoring middle term
    else:
        lst2 = lst[split + 1:]
    # sorting both lists
    lst1.sort()
    lst2.sort()
    # Comparing both the halves
    if lst1 == lst2:
        print('YES')
    else:
        print('NO')
