class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        row_max = [0]*n
        col_max = [0]*m
        
        increment = 0

        for i in range(n):
            for j in range(m):
                val = grid[i][j]
                if val > row_max[i]:
                    row_max[i] = val
                if val > col_max[j]:
                    col_max[j] = val

        for i in range(n):
            for j in range(m):
                val = grid[i][j]
                line = min(row_max[i], col_max[j])
                if val < line:
                    increment += line-val
        
        return increment