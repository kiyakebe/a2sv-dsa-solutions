class Solution:
    def climbStairs(self, n: int) -> int:
        d = {n-1: 1, n-2: 2}
        for i in range(n-3, -1, -1):
            d[i] = d[i+1] + d[i+2]
        return d[0]