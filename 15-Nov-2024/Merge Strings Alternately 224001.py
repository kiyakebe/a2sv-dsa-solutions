# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = len(word1)
        b = len(word2)
        if b<a:
            shorter = b
            remaining = word1[b:]
        else:
            shorter = a
            remaining = word2[a:]
        ans =''
        for i in range(shorter):
            ans += word1[i] + word2[i]
        return ans + remaining