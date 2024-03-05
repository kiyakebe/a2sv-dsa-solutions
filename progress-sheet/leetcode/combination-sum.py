class Solution:
    def __init__(self):
        self.ans = []

    def combination(self, candidates, target, comb, starting):
        _sum = sum(comb)
        if _sum == target:
            self.ans.append(comb[:])
        if _sum >= target:
            return
        
        for i in range(starting, len(candidates)):
            comb.append(candidates[i])
            self.combination(candidates, target, comb, i)
            comb.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combination(candidates, target, [], 0)
        return self.ans