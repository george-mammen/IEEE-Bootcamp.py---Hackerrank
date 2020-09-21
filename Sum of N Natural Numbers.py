"""
Qs:Read N from input and print the sum of first N Natural Numbers.

Sample Input 0
5

Sample Output 0
15
"""

Code:
num=int(input(""))
sum=0
while num > 0:
        sum = sum + num
        num = num - 1
print("{0}".format(sum))
