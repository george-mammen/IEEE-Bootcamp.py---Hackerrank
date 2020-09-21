"""
Qs:Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of hash(t) .

Sample Input 0
2
1 2

Sample Output 0
3713081631934410656

"""
Code:
n=int(raw_input())
a=raw_input()
list=a.split()
for i in xrange(n):
        list[i] = int(list[i])
my_tuple=tuple(list)        
print hash(my_tuple) 
