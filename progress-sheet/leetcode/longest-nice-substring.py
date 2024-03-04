class Solution:
    def helper(self, strg):
        ls = set(strg)
        for c in ls:
            if c.swapcase() not in ls:
                return False
        return True

    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        ans = ''
        for i in range(2, n+1):
            for j in range(n-i+2):
                if self.helper(s[j:j+i]):
                    if len(ans) != len(s[j:j+i]):
                        ans = s[j:j+i]
                    break
        return ans