class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        val = nums[0]
        counter = 0
        for i in range(1, n):
            if nums[i] < val:
                counter += 1
                if i == 1:
                    val = nums[i]
                    continue
                if nums[i] >= nums[i-2]:
                    val = nums[i]
            else:
                val = nums[i]
            if counter > 1:
                return False
        return True