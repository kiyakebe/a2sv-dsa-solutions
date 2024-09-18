# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def compare(self, x1, x2):
        if x1 + x2 > x2 + x1:
            return -1
        return 1

    def largestNumber(self, nums: List[int]) -> str:
        nm = [str(x) for x in nums]

        sorted_nums = sorted(nm, key=cmp_to_key(self.compare))

        if sorted_nums[0] == '0':
            return '0'

        return ''.join(sorted_nums)