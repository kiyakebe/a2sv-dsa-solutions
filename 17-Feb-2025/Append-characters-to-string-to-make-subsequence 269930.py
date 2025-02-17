# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        
        while i < len(t):
            while j < len(s) and s[j] != t[i]:
                j += 1

            if j >= len(s):
                break
            
            j += 1
            i += 1

        return len(t[i:])