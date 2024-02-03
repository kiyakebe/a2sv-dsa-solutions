class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0 for i in range(n+1)]
        ans = [0 for i in range(n)]
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        for i in range(n):
            ans[i] = (nums[i]*i - prefix[i]) + (prefix[-1] - prefix[i]) - nums[i]*(n-i)
        
        return ans