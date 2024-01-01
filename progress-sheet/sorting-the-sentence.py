class Solution:
    def sortSentence(self, s: str) -> str:
        d= {}
        sorted_word = []
        for i in s.split():
            d[int(i[-1])] = i[:-1]
        
        for i in range(1, len(d)+1):
            sorted_word.append(d[i])

        return " ".join(sorted_word)

'''
Time Complexity = O(n)
Space Complexity = O(n)
'''