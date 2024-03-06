class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x - 1
        _max = 0
        if x < 2:
            return x
        while l <= r:
            middle = l + (r-l)//2
            if middle*middle == x:
                return middle
            elif middle*middle < x:
                _max = middle
                l = middle + 1
            else:
                r = middle - 1
        return _max