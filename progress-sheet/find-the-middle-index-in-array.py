class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
            
        for i in range(n):
            if i==0: left = 0
            else: left = nums[i-1]

            if i==n-1: right = 0
            else: right = nums[-1]-nums[i]

            if  left == right:
                return i 

        return -1