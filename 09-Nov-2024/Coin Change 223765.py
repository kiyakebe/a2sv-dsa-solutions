# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def dfs(self, _sum, i):
        if _sum == self.amount:
            return 0
        elif _sum > self.amount or i >= len(self.coins):
            return float("inf")
        
        if (_sum, i) in self.dp:
            return self.dp[(_sum, i)]
        
        inc = self.dfs(_sum + self.coins[i], i)
        exc = self.dfs(_sum, i+1)
        
        self.dp[(_sum, i)] = min(inc+1,exc)
        return self.dp[(_sum, i)]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.amount = amount
        self.dp = {}
        
        ans = self.dfs(0, 0)
        return -1 if ans == float("inf") else ans