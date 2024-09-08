# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n,k,q = map(int,input().split())
pos =[0] *200002
for i in range(n):
    l,r = map(int,input().split())
    pos[l]+=1
    pos[r+1] -=1 

for i in range(2, 200002):
    pos[i] += pos[i-1]

pre=[0] * 200002
c=0    

for i in range(1,200002):  
    if pos[i] >=k:
        c+=1
    pre[i] = c             
for i in range(q):
    l1,r1 = map(int,input().split())
    print(pre[r1]-pre[l1-1])