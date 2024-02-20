class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        _sum = 0
        avg = 0

        for i in range(n):
            _sum += nums[i]
            if nums[i] > avg:
                avg = max(ceil(_sum/(i+1)), avg)
            
        return avg