class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        r = n - 1
        l = n - 1
        count = 0
        while l > 0:
            val = nums[l]
            while nums[l] == val and l > 0:
                l -= 1
            # make it o-index and take the difference
            if nums[l] != val:
                count += n-1- l
            r = l
        return count