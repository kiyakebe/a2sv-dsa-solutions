# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        cnt = 0

        for word in words:
            for cr in word:
                if cr not in allowed_set:
                    break
            else:
                cnt += 1
        
        return cnt