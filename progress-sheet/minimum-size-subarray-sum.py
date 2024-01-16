class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        _min = float("inf")
        _sum = 0
        while r < n or l <= r:
            if _sum < target and r < n:
                _sum += nums[r]
                r += 1
            elif _sum >= target:
                _min = min(_min, r-l)
                _sum -= nums[l]
                l += 1
            else:
                break
        if _min == float("inf"):
            return 0
        return _min