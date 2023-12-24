class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        left_index = 0
        words = []
        for i in spaces:
            words.append(s[left_index:i])
            left_index = i
        words.append(s[left_index:])
        print(words)
        return ' '.join(words)