# Problem: E - Min Divisible Outside Segment - https://codeforces.com/gym/545013/problem/E

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
    l, r, d = map(int, input().split())
    
    if d < l:
        print(d)
    elif d > r:
        print(d)
    else:
        mod = r % d
        
        if mod == 0:
            print(r+d)
        else:
            print(r+(d-mod))
    