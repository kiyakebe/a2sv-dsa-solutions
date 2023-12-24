class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m-1):
            for j in range(1, n-1):
                curr_sum = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
                max_sum = max(max_sum, curr_sum)
        return max_sum