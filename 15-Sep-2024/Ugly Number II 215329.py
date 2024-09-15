# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        vals = [2,3,5]
        uglyHeap = [1]

        visited = set()

        visited.add(1)

        for _ in range(n):
            curr = heappop(uglyHeap)
            for prime in vals:
                new_val = curr*prime
                if new_val not in visited:
                    heappush(uglyHeap, new_val)
                    visited.add(new_val)
        
        return curr