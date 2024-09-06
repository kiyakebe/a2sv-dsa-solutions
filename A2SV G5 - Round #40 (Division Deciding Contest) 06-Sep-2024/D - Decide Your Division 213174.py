# Problem: D - Decide Your Division - https://codeforces.com/gym/543431/problem/D

t = int(input())

for _ in range(t):
    n = int(input())
    
    cnt = 0

    while n % 5 == 0:
        n //= 5
        cnt += 3
    
    while n % 3 == 0:
        n //= 3
        cnt += 2
        
    while n % 2 == 0:
        n //= 2
        cnt += 1
    
    if n > 1:
        print(-1)
    else:
        print(cnt)