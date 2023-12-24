class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n = len(nums)//3
        ans = []
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        for i in d:
            if d[i] > n:
                ans.append(i)
        return ans