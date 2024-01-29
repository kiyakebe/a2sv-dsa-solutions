class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        n = len(fruits)
        
        l = 0
        r = 0

        fruit_count = 0
        _max = 0

        while r < n:
            d[fruits[r]] += 1
            r += 1
            fruit_count += 1
            if len(d) <= 2:
                _max = max(_max, fruit_count)
            else:
                while len(d) > 2:
                    d[fruits[l]] -= 1
                    if d[fruits[l]] == 0:
                        del d[fruits[l]]
                    l += 1
                    fruit_count -= 1
        return max(_max, fruit_count)