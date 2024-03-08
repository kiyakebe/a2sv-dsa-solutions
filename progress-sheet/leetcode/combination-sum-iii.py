class Solution:
    def __init__(self):
        self.ans = set()

    def findCombination(self, temp, k, n, starting):
        if len(temp) == k and sum(temp) == n:
            self.ans.add(tuple(temp[:]))
            return
        elif len(temp) > k or sum(temp) > n:
            return

        for i in range(starting, 10):
            temp.append(i)
            self.findCombination(temp, k, n, i+1)
            temp.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.findCombination([], k, n, 1)

        comb = [list(i) for i in self.ans]
        
        return comb 