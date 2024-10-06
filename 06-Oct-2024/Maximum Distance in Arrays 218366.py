# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution(object):
    def maxDistance(self, arrays):
        _min = arrays[0][0]
        _max = arrays[0][-1]
        diff = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            diff = max(diff, abs(arr[-1] - _min), abs(_max - arr[0]))
            _min = min(_min, arr[0])
            _max = max(_max, arr[-1])

        return diff