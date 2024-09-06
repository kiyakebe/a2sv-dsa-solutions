# Problem: B - Diversity - https://codeforces.com/gym/543431/problem/B

from collections import Counter
s = input()
k = int(input())

cnt = Counter(s)

if len(s) < k:
    print("impossible")
else:
    ln = len(cnt)
    change = k - ln
    if change >= 0:
        print(change)
    else:
        vals = sorted(cnt.values())
        print(0)
