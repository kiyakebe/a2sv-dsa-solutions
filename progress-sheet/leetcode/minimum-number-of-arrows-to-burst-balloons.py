class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])

        count = 0
        end = float("-inf")
        for i in points:
            if i[0] > end:
                count += 1
                end = i[1]
        return count