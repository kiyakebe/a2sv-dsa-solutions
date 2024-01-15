class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        _max = 0
        d = defaultdict(int)
        while r < len(nums):
            _max = max(_max, d[1] + d[0])
            d[nums[r]]+=1
            if d[0] == k+1:
                while d[nums[r]] == k+1 and l<=r:
                    d[nums[l]] -= 1
                    l += 1
            r += 1
        return max(_max, d[1] + d[0])
