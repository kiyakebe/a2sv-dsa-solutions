class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        _max = 0
        _sum = 0
        n = len(cardPoints)
        for i in range(n-k, n):
            _sum += cardPoints[i]
        for i in range(k):
            _max = max(_max, _sum)
            _sum += cardPoints[i]
            _sum -= cardPoints[n-k+i]
        return max(_sum, _max)
