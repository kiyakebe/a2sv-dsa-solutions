class Solution:
    def __init__(self):
        self.ans = []

    def backtrack(self, com, i, n, k):
        if i > n+1:
            return
        if len(com) == k:
            self.ans.append(com[:])
            return

        com.append(i)
        self.backtrack(com, i+1, n, k)
        com.pop()
        self.backtrack(com, i+1, n, k)

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack([], 1, n, k)
        return self.ans