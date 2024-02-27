class Solution:
    def __init__(self):
        self.ans = 0
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return int(self.ans)
        half = 2**(n-2)
        if k>half:
            k-=half
            self.ans = not self.ans
        return  self.kthGrammar(n-1, k)
  