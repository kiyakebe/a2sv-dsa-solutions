class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(int)
        d[0] = 1

        nums = [0] + nums
        count = 0
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i]-goal in d:
                count += d[nums[i]-goal]
            d[nums[i]]+=1
        return count