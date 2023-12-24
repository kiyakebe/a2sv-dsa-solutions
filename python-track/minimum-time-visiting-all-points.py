class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_time = 0
        for i in range(1, n):
            min_time += max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))
        return min_time