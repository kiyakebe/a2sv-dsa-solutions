class Solution:
    def numberOfWays(self, s: str) -> int:
        d = defaultdict(int)
        n = len(s)
        for i in range(n-1, -1, -1):
            if s[i] == '1':
                d['1'] += 1
                d['101'] += d['01']
                d['10'] += d['0']
            else:
                d['0'] += 1
                d['010'] += d['10']
                d['01'] += d['1']
        
        return d['010'] + d['101']