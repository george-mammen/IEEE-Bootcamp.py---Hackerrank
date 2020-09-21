"""
Qs: You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Sample Input
this is a string   

Sample Output
this-is-a-string

"""
Code:
def split_and_join(line):
    line=line.split()
    line='-'.join(line)
    return line
