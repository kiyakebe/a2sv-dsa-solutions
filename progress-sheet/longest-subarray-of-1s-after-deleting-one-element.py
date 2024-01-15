class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        _max = 0
        d = defaultdict(int)
        while r < len(nums):
            d[nums[r]] += 1
            if d[0] == 2:
                _max = max(_max, d[1])
                while d[nums[r]] == 2 and l <=r:
                    d[nums[l]] -= 1
                    l += 1
            r += 1
        if d[0] == 0:
            # no zero and one number must be deleted
            return d[1] - 1
        return max(_max, d[1])