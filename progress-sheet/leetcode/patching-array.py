class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i, _sum, count = 0, 0, 0
        while _sum < n:
            if i < len(nums) and nums[i] <= (_sum+1):
                _sum += nums[i]
                i += 1
            else:
                count += 1
                _sum += (_sum+1)
            print(_sum, count)
        return count
