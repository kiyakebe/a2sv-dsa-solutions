class Solution:
    def __init__(self):
        self.ans = []

    def permutate(self, nums, n, perm):
        if len(perm) == n:
            self.ans.append(perm[:])
            return

        for i in nums:
            if i not in perm:
                perm.append(i)
                self.permutate(nums, n, perm)
                perm.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutate(nums, len(nums), [])

        return self.ans