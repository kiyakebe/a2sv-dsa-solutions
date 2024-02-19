class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        odd = False
        longest = 0
        for v, c in count.items():
            longest += c
            if c%2 == 1:
                longest -= 1
                odd = True
        if odd:
            return longest + 1
        return longest