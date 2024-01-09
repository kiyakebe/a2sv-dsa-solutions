class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        _max = 1
        d = defaultdict(int)
        start = 0
        end = 0
        if len(s) == 0:
            return 0
        while end < len(s):
            d[s[end]] += 1
            if d[s[end]] == 1:
                count += 1
                end += 1
            else:
                _max = max(_max, count)
                while d[s[end]] == 2:
                    d[s[start]] -= 1
                    start += 1
                    count -= 1
                # the value that made the value 2 is not counted
                count += 1
                end += 1

        return max(count, _max)
            
