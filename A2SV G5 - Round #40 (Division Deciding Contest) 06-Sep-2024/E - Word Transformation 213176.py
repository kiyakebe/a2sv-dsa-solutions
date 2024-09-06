# Problem: E - Word Transformation - https://codeforces.com/gym/543431/problem/E

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
    word1, word2 = input().split()
    visited = set()
    w1 = list(reversed(word1))
    w2 = list(reversed(word2))
    
    x, y = 0, 0
    
    construct = []
    
    while x < len(w1) and y < len(w2):
        if w2[y] == w1[x]:
            if w2[y] in visited:
                break
            construct.append(w2[y])
            y += 1
            x += 1
        else:
            visited.add(w1[x])
            x += 1
    
    if ''.join(reversed(construct)) == word2:
        print("YES")
    else:
        print("NO")