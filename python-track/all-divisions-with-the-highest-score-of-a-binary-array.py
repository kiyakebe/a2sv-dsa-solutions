class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = {}
        ones = sum(nums)
        # print(ones)
        zeros = 0
        max_val = ones
        for i in range(n+1):
            val = ones + zeros
            max_val = max(max_val, val)
            if val not in d:
                d[val] = []
            d[val].append(i)

            if i!=n:
                if nums[i] == 1: ones -= 1
                else: zeros += 1
        return d[max_val]
        