# Problem: C - Lab Renovation Sum Check - https://codeforces.com/gym/545013/problem/C

import sys
 
def input():
    return sys.stdin.readline().strip()
 
def print(*output):
    output = ' '.join(list(map(str, output)))
    return sys.stdout.write(output + '\n')
 
def lsi():
    return [int(i) for i in input().split()]
 
def ls():
    return list(input().split())
 
def debug(*args):
    print(args)
 
 
n = int(input())
matrix = []
 
for _ in range(n):
    matrix.append(lsi())
 
cols_set = [set() for _ in range(n)]
 
for i in range(n):
    for j in range(n):
        cols_set[j].add(matrix[i][j])
 
flag = False
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            continue
        
        for k in range(n):
            if k == j:
                continue
            
            curr_val = matrix[i][j] - matrix[i][k]
            if curr_val in cols_set[j]:
                break
        else:
            flag = True
            break
    if flag:
        break
 
 
if flag:
    print("No")
else:
    print("Yes")