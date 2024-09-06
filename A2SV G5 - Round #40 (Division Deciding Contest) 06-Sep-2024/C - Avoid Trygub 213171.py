# Problem: C - Avoid Trygub - https://codeforces.com/gym/543431/problem/C

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


t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    s_ls = list(s)
    
    cnt = 0
    
    for i in range(n):
        if s_ls[i] == 't':
            s_ls[i] = ''
            cnt += 1
    
    s_ls +=(['t']*cnt)
    
    print(''.join(s_ls))