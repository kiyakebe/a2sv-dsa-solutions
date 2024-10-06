# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        directions = [[-1,0], [0,-1], [1,0], [0,1]]
        
        def inBound(x, y):
            return 0 <= x < m and 0 <= y < n

        possible = True
        def traverse(i, j):
            nonlocal possible
            grid2[i][j] = 2
            if grid1[i][j] != 1:
                possible = False

            for x, y in directions:
                ni, nj = i + x, j + y
                if inBound(ni, nj) and grid2[ni][nj] == 1:
                    traverse(ni, nj)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    traverse(i, j)
                    if possible:
                        count += 1
                    possible = True
        
        return count