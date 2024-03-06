class Solution:
    # def __init__(self):
    #     self.ans

    # def search(self, nums):


    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        pos = 0
        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] < target:
                left = mid+1
                pos = left
            elif nums[mid] > target:
                right = mid-1
            elif nums[mid] == target:
                pos = mid
                right = mid-1

        return pos