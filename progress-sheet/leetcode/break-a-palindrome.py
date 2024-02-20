class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)

        if n == 1:
            return ""
        middle_bound = n//2
        ls = list(palindrome)

        for i in range(middle_bound):
            if ls[i] != 'a':
                ls[i] = 'a'
                break
        else:
            ls[-1] = 'b'
        
        return "".join(ls)