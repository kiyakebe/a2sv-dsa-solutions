# Problem: Maximal AND - https://codeforces.com/problemset/problem/1669/H

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
    n, k = map(int, input().split())

    nums = lsi()
    cnt = [0]*31
    for i in range(n):
        for j in range(31):
            if nums[i]&(1<<j):
                cnt[j] += 1

    for i in range(30, -1, -1):
        if k >= n-cnt[i]:
            k -= (n-cnt[i])
            cnt[i] = n
    
    for i in range(31):
        if cnt[i] == n:
            cnt[i] = '1'
        else:
            cnt[i] = '0'
    
    print(int(''.join(reversed(cnt)), 2))