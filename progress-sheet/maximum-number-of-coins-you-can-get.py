class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        # pick one from the left and two from the right
        starting = len(piles)//3
        for i in range(starting, len(piles), 2):
            ans += piles[i]
        return ans