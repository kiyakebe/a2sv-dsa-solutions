# Problem: B - Chore Partitioning - https://codeforces.com/gym/545013/problem/B

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
    curr = 1
    AB = [0, 0]
    turn = 0
    while n - sum(AB) >= curr:
        AB[turn%2] += curr
        curr += 4
        turn += 1
    
    AB[turn%2] += n - sum(AB)
    
    print(*AB)