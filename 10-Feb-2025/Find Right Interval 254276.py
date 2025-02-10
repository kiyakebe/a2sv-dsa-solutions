# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        right = [[intervals[i][0],i] for i in range(n)]
        right.sort()
        ans = [-1]*n
        for i in range(n):
            c = bisect_left(right, [intervals[i][1]])
            if c < n:
                ans[i] = right[c][1]
        
        return ans