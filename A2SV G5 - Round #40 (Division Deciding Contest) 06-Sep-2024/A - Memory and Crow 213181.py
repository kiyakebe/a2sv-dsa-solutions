# Problem: A - Memory and Crow - https://codeforces.com/gym/543431/problem/A

import sys

def input():
    return sys.stdin.readline().strip()

def print(*output):
    output = ' '.join(list(map(str, output)))
    return sys.stdout.write(output + '\n')

def lsi():
    return [int(i) for i in input().split()]

n = int(input())

nums = lsi()

for i in range(n-1):
    nums[i] += nums[i+1]

print(*nums)