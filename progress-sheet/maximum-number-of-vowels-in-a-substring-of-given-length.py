class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowels = {'a', 'e', 'o', 'i', 'u'}
        for i in range(k):
            if s[i] in vowels:
                count += 1
        _max = count
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            if _max < count:
                _max = count
        return _max 