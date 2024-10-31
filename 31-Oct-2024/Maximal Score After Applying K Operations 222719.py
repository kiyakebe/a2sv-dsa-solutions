# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        heap = [-x for x in nums]
        heapify(heap)

        while k:
            val = -heappop(heap)
            score += val
            heappush(heap, -((val+2)//3))
        
            k -= 1

        return score