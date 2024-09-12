# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0]*(n-2) for _ in range(m-2)]

        for i in range(m-2):
            for j in range(n-2):
                ans[i][j] = max(grid[i][j], grid[i][j+1], grid[i][j+2],
                                grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                                grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2])
        
        return ans