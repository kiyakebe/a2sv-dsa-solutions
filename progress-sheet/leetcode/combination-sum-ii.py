class Solution:
    def __init__(self):
        self.ans = []
        self.visited = set()

    def combination(self, candidates, target, comb, starting):
        _sum = sum(comb)
        if _sum == target:
            if tuple(comb) not in self.visited:
                self.ans.append(comb[:])
                self.visited.add(tuple(comb))

        if _sum >= target:
            return
        
        
        for i in range(starting, len(candidates)):
            if i > starting and candidates[i] == candidates[i-1]:
                continue
            comb.append(candidates[i])
            self.combination(candidates, target, comb, i+1)
            comb.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        self.combination(candidates, target, [], 0)
        return self.ans