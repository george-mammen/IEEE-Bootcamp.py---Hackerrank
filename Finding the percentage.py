"""
Sample Input 0
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 0
56.00

Sample Input 1
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

Sample Output 1
26.50
"""
Code:
def avg(lst):
    return(lst[0]+lst[1]+lst[2])/3
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
print(f'{avg(student_marks[query_name]):.2f}')
