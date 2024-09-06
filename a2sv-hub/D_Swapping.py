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
    n, x, m = map(int, input().split())
    
    interval = [x,x]
    
    for i in range(m):
        l, r = map(int, input().split())
        
        if interval[0] <= l <= interval[1] or interval[0] <= r <= interval[1]:
            interval[0] = min(interval[0], l, r)
            interval[1] = max(interval[1], l, r)
        elif l <= interval[0] <= r:
            interval = [l, r]
    
    print(interval[1]-interval[0]+1)