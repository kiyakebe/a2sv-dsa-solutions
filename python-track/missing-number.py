class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_num_set = {x for x in range(n+1)}
        nums_set = set(nums)
        missing = total_num_set - nums_set
        return list(missing)[0]