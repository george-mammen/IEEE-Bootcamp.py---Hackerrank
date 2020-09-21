"""
Qs: Read a list and print the number of elements divisible by 3.

Input Format
First line contains n the number of elements in the list. The following n lines contains the elements of the list.

Sample Input 0
5
1
7
3
6
5

Sample Output 0
2

"""

Code:  
list= []
count=0
n=int(input())
for i in range(0, n): 
    numbers= int(input()) 
    list.append(numbers)
    if numbers % 3 ==0:
        count=count+1
print(count) 
