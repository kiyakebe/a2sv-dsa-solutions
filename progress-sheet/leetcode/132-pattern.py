class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        data = float("-inf")

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < data:
                return True
            
            while stack and stack[-1] < nums[i]:
                data = stack.pop()
            stack.append(nums[i])
        return False

# 1 3 4 2 4 3