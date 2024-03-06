class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        n = len(heaters)
        _max = float("-inf")
        
        for i in houses:
            left = bisect_left(heaters, i)
            _min = float("inf")
            if left > 0:
                _min = i-heaters[left-1]
            if left < n:
                _min = min(_min, heaters[left]-i)
            _max = max(_max, _min)

        return _max