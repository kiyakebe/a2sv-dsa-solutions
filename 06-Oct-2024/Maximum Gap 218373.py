# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        heapify(nums)
        num1 = heappop(nums)
        ans = 0
        while nums:
            num2 = heappop(nums)
            ans = max(ans, num2-num1)
            num1 = num2
        
        return ans  