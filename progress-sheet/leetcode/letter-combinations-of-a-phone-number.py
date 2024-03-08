class Solution:
    def __init__(self):
        self.ans = []
        self.d = {
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
            }

    def make_combination(self, digits, index, temp):
        if index > len(digits):
            return

        if len(temp) == len(digits):
            self.ans.append("".join(temp[:]))
            return

        for i in range(0, len(self.d[digits[index]])):
            temp.append(self.d[digits[index]][i])
            self.make_combination(digits, index+1, temp)
            temp.pop()      
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return

        self.make_combination(digits, 0, [])
        return self.ans