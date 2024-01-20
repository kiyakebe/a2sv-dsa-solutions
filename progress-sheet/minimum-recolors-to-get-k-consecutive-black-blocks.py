class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        d = defaultdict(int)
        n = len(blocks)
        for i in range(k):
            d[blocks[i]] += 1
        _min = d['W']
        for i in range(k, n):
            d[blocks[i]] += 1
            d[blocks[i-k]] -= 1
            _min = min(_min, d['W'])
        return _min
