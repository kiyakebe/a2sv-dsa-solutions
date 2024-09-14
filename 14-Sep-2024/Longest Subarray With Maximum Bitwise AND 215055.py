# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        _max = max(nums)

        ans = 1
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == _max:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        
        return ans