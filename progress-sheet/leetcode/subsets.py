class Solution:
    def __init__(self):
        self.subset = [[]]

    def createSubset(self, n):
        x = len(self.subset)
        for i in range(x):
            temp = self.subset[i].copy()
            temp.append(n) 
            self.subset.append(temp)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        for i in nums:
            self.createSubset(i)
    
        return self.subset