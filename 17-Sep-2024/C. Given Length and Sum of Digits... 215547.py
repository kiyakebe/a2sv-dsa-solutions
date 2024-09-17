# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m, s = map(int, input().split())
z = s
if s == 0 and m == 1:
    print(0, 0)
elif s == 0 or s/m > 9:
    print(-1, -1)
else:
    ans = ['0']*m
    min_max = []    
    
    for i in range(m-1, -1, -1):
        if s > 9:
            ans[i] = '9'
            s -= 9
        else:
            if i == 0:
                ans[i] = str(s)
            else:
                ans[i] = str(s-1)
                ans[0] = '1'
                break
    
    min_max.append(''.join(ans))
    
    ans = ['0']*m
    
    for i in range(m):
        if z > 9:
            ans[i] = '9'
            z -= 9
        else:
            ans[i] = str(z)
            break
        
    min_max.append(''.join(ans))
    print(*min_max)