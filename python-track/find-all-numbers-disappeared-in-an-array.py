class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        appearing_nums = set(nums)
        ans = []
        for i in range(1, n+1):
            if i not in appearing_nums:
                ans.append(i)
        return ans
