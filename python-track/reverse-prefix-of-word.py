class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ''
        if(ch in word):
            index = word.index(ch)
            return ''.join(reversed(word[:index+1])) + word[index+1:]
        else:
            return word
        return 