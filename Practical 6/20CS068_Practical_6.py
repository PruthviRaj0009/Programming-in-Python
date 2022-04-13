'''
20CS068
Pruthvi Raj

You are given n words. Some words may repeat. For each word, output its
number of occurrences. The output order should correspond with the input order
of appearance of the word. See the sample input/output for clarification.

Sample Input
4
bcdef
abcdefg
bcde
bcdef

Sample Output
3
2 1 1

Explanation:
There are 3 distinct words. Here, "bcdef" appears twice in the input
at the first and last positions. The other words appear once each. The order of the
first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the
output.
'''

# taking input from user for testcases
testcases = int(input())
# making a dictionary
count_dict = {}
# making a list
v = []
# using for loop
for i in range(testcases):
    # taking input from user
    s = input()
    # taking in list
    v.append(s)
    # codititon
    if s in count_dict:
        count_dict[s] += 1
    else:
        count_dict[s] = 1

# printing output 
print(len(count_dict))
print(' '.join([str(count_dict[s]) for s in count_dict]))
