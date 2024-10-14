# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_cnt = [0 for _ in range(len(s)+1)]
        if s[0] == 'a': a_cnt[1] += 1
        for i in range(len(s)):
            if s[i] == 'a':
                a_cnt[i+1] = a_cnt[i] + 1
            else:
                a_cnt[i+1] = a_cnt[i]
        
        _min = float("inf")
        for i in range(len(s)+1):
            left = i - a_cnt[i]
            right = a_cnt[-1] - a_cnt[i]
            curr_cost = left + right
            
            _min = min(_min, curr_cost)

        return _min



