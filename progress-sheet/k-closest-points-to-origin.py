class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        val = defaultdict(list)
        count = defaultdict(int)

        # we can use the sum for comparison

        for x, y in points:
            val[pow(x,2)+pow(y,2)].append([x,y])
            count[pow(x,2)+pow(y,2)] += 1
        
        ans = []
        c = 0
        for i in sorted(val.keys()):
            if c < k:
                ans += val[i]
                c += count[i]
            else: break

        return ans
        