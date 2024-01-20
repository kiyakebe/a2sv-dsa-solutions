class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        d ={
            'T': 0,
            'F': 0
        }
        l = 0
        r = 1
        _max = 0
        n = len(answerKey)
        d[answerKey[0]] += 1
        while r < n:
            d[answerKey[r]] += 1
            while min(d.values()) > k:
                d[answerKey[l]] -= 1
                l += 1
            _max = max(_max, r-l+1)
            r += 1

        return max(_max, r-l)