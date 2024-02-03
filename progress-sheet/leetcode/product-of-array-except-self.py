class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1 for i in range(n + 1)] # left offset
        postfix = [1 for i in range(n + 1)] # right offset
        ans = [0 for i in range(n)]

        for i in range(n):
            prefix[i+1] = prefix[i] * nums[i]
            postfix[n-i-1] = postfix[n-i] * nums[n-i-1]

        for i in range(n):
            ans[i] = prefix[i]*postfix[i+1]

        return ans