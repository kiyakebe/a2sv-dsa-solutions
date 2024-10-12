# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        groups = 1
        heappush(heap, intervals[0][1])

        for interval in intervals[1:]:
            if heap[0] < interval[0]:
                heappop(heap)
                heappush(heap, interval[1])
            else:
                groups += 1
                heappush(heap, interval[1])

        return groups