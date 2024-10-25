# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        lad = []
        heapify(lad)
        total_bricks_yet = 0

        for i in range(1, len(heights)):
            jump = heights[i] - heights[i-1]
            if jump > 0:
                if len(lad) < ladders:
                    heappush(lad, jump)
                else:
                    heappush(lad, jump)
                    total_bricks_yet += lad[0]
                    heappop(lad)

                    if total_bricks_yet > bricks:
                        return i-1
        
        return len(heights)-1
