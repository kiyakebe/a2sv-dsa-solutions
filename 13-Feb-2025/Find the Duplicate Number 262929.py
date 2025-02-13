# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = nums[0]

        for i in nums[1:]:
            ans ^= i
        
        for i in range(1, len(nums)):
            ans ^= i
        
        return ans