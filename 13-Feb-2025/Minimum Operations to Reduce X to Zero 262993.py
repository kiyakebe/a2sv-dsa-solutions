# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = 0
        n = len(nums)
        window = 0
        diff = sum(nums)-x
        _min = float("inf")
        
        if diff < 0:
            return -1

        for right in range(n):
            window += nums[right]
            while window > diff:
                window -= nums[left]
                left += 1
            
            if window == diff:
                _min =min(_min, n-(right-left+1))
        
        if _min == float("inf"):
            return -1
        return _min