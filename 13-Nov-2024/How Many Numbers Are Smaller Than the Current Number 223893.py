# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smallet_counter = {}
        sorted_nums = sorted(nums)
        n = len(nums)
        ans = []
        
        for i in range(n):
            if sorted_nums[i] not in smallet_counter:
                smallet_counter[sorted_nums[i]] = i

        ans = [smallet_counter[num] for num in nums]

        return ans