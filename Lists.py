"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Sample Input 0
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

"""

Code:
list= []
for i in range(int(raw_input())):
    a = raw_input().split()
    for i in range(1,len(a)):
        a[i] = int(a[i])
        
    if a[0] == "append":
        list.append(a[1])
    elif a[0] == "extend":    
        list.extend(a[1:])
    elif a[0] == "insert":
        list.insert(a[1],a[2])
    elif a[0] == "remove":
        list.remove(a[1])
    elif a[0] == "pop":
        list.pop()
    elif a[0] == "index":
        print list.index(a[1])
    elif a[0] == "count":
        print list.count(a[1])
    elif a[0] == "sort":
        list.sort()
    elif a[0] == "reverse":
        list.reverse()
    elif a[0] == "print":
        print list
