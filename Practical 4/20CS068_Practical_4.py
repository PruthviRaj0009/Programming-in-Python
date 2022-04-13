'''
20CS068
Pruthvi Raj

Find runner-up from given list

Sample Input
5
2 3 6 6 5

Sample Output
5

Explanation:
Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5.
Hence, we print 5 as the runner-up score. 
'''

# taking integer input from user for number that user will input in list
n = int(input())
# taking list integer input of numbers from user
l = list(map(int, input().split()))[:n]
# sorting list
l.sort()
# printing second maximum score from list
print(l[-2])
