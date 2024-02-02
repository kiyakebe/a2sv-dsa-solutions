class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips_ps = [0 for i in range(1002)]
        for c, f, t in trips:
            trips_ps[f+1] += c
            trips_ps[t+1] -= c
        for i in range(1, 1002):
            ps = trips_ps[i] + trips_ps[i-1]
            if ps > capacity:
                print(ps, capacity)
                print(trips_ps)
                return False
            trips_ps[i] = ps
        return True