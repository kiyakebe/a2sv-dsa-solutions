# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        while columnNumber > 0:
            curr = columnNumber%26
            ans.append(alpha[curr-1])
            columnNumber = (columnNumber-1)//26
        
        return ''.join(ans[::-1])