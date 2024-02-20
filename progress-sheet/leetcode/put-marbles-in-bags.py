class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        for i in range(1, len(weights)):
            weights[i-1] += weights[i]
        
        _sum = weights[0] + weights[-1]

        arr = weights[:-1]
        arr.sort()

        l = len(arr)
        return sum(arr[l-(k-1):]) - sum(arr[:k-1])