"""
Qs:Read N from input and print the first N odd numbers

Sample Input 0
3

Sample Output 0
1
3
5

"""

Code :
num=int(input(""))
for i in range(1,num+num,2):
    if((i % 2) ==1):
        print("{0}".format(i)) 
