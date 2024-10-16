# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/513152/problem/C

for i in range(int(input())):
    n, m = map(int, input().split())
    s = input()
    w = input()
    ws = 0
    for i in w:
        ws += ord(i)
    
    ls = []
    ans = []
    for i in s:
        ls.append(ord(i))
        
    for i in range(1, n):
        ls[i] = ls[i]+ls[i-1]
    
    for i in range(m-1, n):
        if i == m-1:
            if ls[m-1] == ws:
                ans.append("YES")
                break
        if ls[i] - ls[i-m] == ws:
            ans.append("YES")
            break
    else:
        ans.append("NO")
        
    for i in ans:
        print(i)
