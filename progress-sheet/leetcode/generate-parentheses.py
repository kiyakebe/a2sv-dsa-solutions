class Solution:
    def __init__(self):
        self.ans = []

    def generate(self,  paren, n, opened, closed):
        if opened == closed == n:
            self.ans.append(''.join(paren[:]))
            return        

        if opened < n:
            paren.append('(')
            self.generate(paren, n, opened+1, closed)
            paren.pop()
            
        if closed < opened:
            paren.append(')')
            self.generate(paren, n, opened, closed+1)
            paren.pop()


    def generateParenthesis(self, n: int) -> List[str]:
        self.generate([], n, 0, 0)

        return sorted(self.ans)