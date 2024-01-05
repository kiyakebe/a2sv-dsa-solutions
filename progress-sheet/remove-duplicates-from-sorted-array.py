class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = [nums[0]]
        for i in range(1, len(nums)):
            if ans [-1] != nums[i]:
                ans.append(nums[i])
        nums[:] = ans
        return len(ans)