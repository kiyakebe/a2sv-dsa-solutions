class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        _max = 0
        _sum = 0
        l = 0
        r = 0
        d = defaultdict(int)
        while r < len(nums):
            _sum += nums[r]
            d[nums[r]] += 1
            if d[nums[r]] == 2:
                _max = max(_max, _sum - nums[r])
                while d[nums[r]] == 2:
                    d[nums[l]] -= 1
                    _sum -= nums[l]
                    l += 1
            r += 1
        return max(_max, _sum)