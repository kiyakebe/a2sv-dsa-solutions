class Solution:
    def first(self, nums, x, n):
        low = 0
        high = n - 1
        res = -1
    
        while (low <= high):
            mid = (low + high) // 2
    
            if nums[mid] > x:
                high = mid - 1
            elif nums[mid] < x:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
        return res

    def last(self, nums, x, n):
        low = 0
        high = n - 1
        res = -1
    
        while(low <= high):
            mid = (low + high) // 2
    
            if nums[mid] > x:
                high = mid - 1
            elif nums[mid] < x:
                low = mid + 1
            else:
                res = mid
                low = mid + 1
        return res
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        return [self.first(nums, target, n), self.last(nums, target, n)]