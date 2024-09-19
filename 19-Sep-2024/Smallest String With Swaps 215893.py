# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class UnionFind:
    def __init__(self, word, size) -> None:
        self.word = word
        self.n = size
        self.parent = {i:i for i in range(size)}
        self.sequence = {i: [word[i]] for i in range(size)}
        self.size = {i:1 for i in range(size)}
    
    def find(self,x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        if self.size[x] > self.size[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
            self.sequence[x] += self.sequence[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]
            self.sequence[y] += self.sequence[x]
    
    def heapify_all(self):
        for i in range(self.n):
            heapify(self.sequence[i])
    
    def construct(self):
        ans = list(self.word)
        for i in range(self.n):
            parent = self.find(i)
            c = heappop(self.sequence[parent])
            ans[i] = c
        
        return ''.join(ans)

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(s, len(s))
        for i in pairs:
            uf.union(i[0], i[1])

        # heapify all groups
        uf.heapify_all()

        return uf.construct()