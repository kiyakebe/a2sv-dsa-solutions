class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(2, n):
            for j in range(i-1, 0, -1):   
                third = nums[i] - nums[j] + 1
                index = bisect_left(nums, third)
                if index < j:
                    count += j - index
                else:
                    break

        return count
