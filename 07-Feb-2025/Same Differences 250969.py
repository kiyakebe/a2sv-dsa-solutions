# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

import sys
from collections import defaultdict

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

for i in range(t):
    cnt = defaultdict(int)
    n = int(input())
    nums = lsi()
    
    for i in range(n):
        cnt[nums[i]-i] += 1

    ans = 0
    
    for val in cnt.items():
        ans += (val[1] * (val[1]-1)) // 2    
    
    print(ans)