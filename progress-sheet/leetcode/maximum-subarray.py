class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = float("-inf")
        curr_sum = 0

        for i in nums:
            curr_sum += i
            largest_sum = max(largest_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        
        return largest_sum