# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        
        for i in range(n):
            for j in range(n):
                heappush(heap, matrix[j][i])
        
        for i in range(k-1):
            heappop(heap)
        
        return heappop(heap)