class Solution:
    def __init__(self):
        self.power_set = []

    def createSubset(self, nums, n, i, subset):
        if i == n:
            self.power_set.append(subset[:])
            return

        subset.append(nums[i])
        self.createSubset(nums, n, i+1, subset)
        subset.pop()

        while i+1 < n and nums[i] == nums[i+1]:
            i += 1

        self.createSubset(nums, n, i+1, subset)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        self.createSubset(nums, n, 0, [])

        return self.power_set
