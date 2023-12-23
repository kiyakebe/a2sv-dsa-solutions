class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set('qwertyuiop')
        second = set('asdfghjkl')
        third = set('zxcvbnm')
        
        ans = []

        for i in words:
            word = set(i.lower())
            if word.issubset(first) or word.issubset(second) or word.issubset(third):
                ans.append(i)
        return ans
