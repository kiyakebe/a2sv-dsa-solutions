class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        nums = [int(n) for n in list(s)]
        for i in range(1, len(nums)):
            left = nums[0:i].count(0); right = nums[i:].count(1)
            if max_score < left+right: max_score = left+right
        return max_score