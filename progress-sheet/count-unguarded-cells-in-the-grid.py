class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[[0,0] for _ in range(n)] for _ in range(m)]
        
        # put walls and guards on their place
        for i in walls:
            grid[i[0]][i[1]] = [-1 ,-1] 
        for i in guards:
            grid[i[0]][i[1]] = [1, 1]

        # to check the reverse iteration
        x = m-1
        y = n-1
        for i in range(0, m):
            for j in range(0, n):
                if i==0 and j==0:
                    continue
                elif i == 0:
                    if grid[i][j-1][0] == 1 and grid[i][j][0] != -1:
                        grid[i][j][0] = 1
                    # reverse
                    if grid[x-i][y-j+1][0] == 1 and grid[x-i][y-j][0] != -1:
                        grid[x-i][y-j][0] = 1
                    
                elif j == 0:
                    if grid[i-1][j][1] == 1 and grid[i][j][1] != -1:
                        grid[i][j][1] = 1
                    # reverse
                    if grid[x-i+1][y-j][1] == 1 and grid[x-i][y-j][1] != -1:
                        grid[x-i][y-j][1] = 1
                else:
                    if grid[i-1][j][1] == 1 and grid[i][j][1] != -1:
                        grid[i][j][1] = 1
                    if grid[i][j-1][0] == 1 and grid[i][j][0] != -1:
                        grid[i][j][0] = 1
                    
                    # reverse
                    if grid[x-i+1][y-j][1] == 1 and grid[x-i][y-j][1] != -1:
                        grid[x-i][y-j][1] = 1

                    if grid[x-i][y-j+1][0] == 1 and grid[x-i][y-j][0] != -1:
                        grid[x-i][y-j][0] = 1

        counter = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == [0,0]:
                    counter += 1
        for i in range(m):
            print(grid[i])
        return counter