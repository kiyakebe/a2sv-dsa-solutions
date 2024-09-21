# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverse_s(self, nums, l, r):
        if l >= r:
            return
        nums[l], nums[r] = nums[r], nums[l]
        self.reverse_s(nums, l+1, r-1)
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        self.reverse_s(s, l, r)