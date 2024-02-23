class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        st = []

        for i in range(2*n):
            index = i%n
            while st and  nums[index] > nums[st[-1]]:
                ans[st.pop()] = nums[index]
            if i < n:
                st.append(i)
        return ans