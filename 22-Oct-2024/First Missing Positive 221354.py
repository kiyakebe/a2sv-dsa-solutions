# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] > 0 and nums[i] <= n:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        return 0