class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)

        x = nums[0]
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = left + (right - left)//2
            if nums[mid] > x:
                left = mid + 1
            elif nums[mid] < x:
                x = nums[mid]
                right = mid - 1
           
        return x