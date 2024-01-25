class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        count = 0
        nums = [0] + nums

        for i in range(1, len(nums)):

            nums[i] += nums[i-1]
            if nums[i]-k in d:
                count += d[nums[i]-k]
            d[nums[i]] += 1

        return count