class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        # pm = prefix_sum_matrix
        self.pm = [[0 for i in range(self.n+1)] for i in range(self.m+1)]
        
        for i in range(1, self.m+1):
            for j in range(1, self.n+1):
                self.pm[i][j] = self.pm[i-1][j] + self.pm[i][j-1] + matrix[i-1][j-1] - self.pm[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pm[row2+1][col2+1] - self.pm[row2+1][col1] - self.pm[row1][col2+1] + self.pm[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)