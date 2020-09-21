"""
Qs: Read a list and print the smallest element.

Input Format
First line contains n the number of elements in the list. The following n lines contains the elements of the list.

Sample Input 0
5
8
4
7
4
5

Sample Output 0
4

"""

Code:
numbers=[]
n=int(input())
for i in range(0,n):                      
     elements = int(input())
     numbers.append(elements) 
print(min(numbers)) 
