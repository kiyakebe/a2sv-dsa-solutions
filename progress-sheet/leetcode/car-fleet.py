class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        n = len(position)
        for i in range(n):
            d[position[i]] = speed[i]
        
        position.sort()
        time = [0]*n
        for i in range(n):
            time[i] = (target - position[i]) / d[position[i]]
        
        count = 1
        _max = time[-1]

        for i in range(n-1, -1, -1):
            if _max < time[i]:
                count += 1
                _max  = time[i]

        return count