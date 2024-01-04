class Solution:

        def check_box(self, row: int, col: int, board: List[List[str]]) -> bool:
            r = (row // 3) * 3
            c = (col // 3) * 3
            val = board[row][col]

            for i in range(r, r+3):
                for j in range(c, c+3):
                    if (i,j) != (row, col):
                        if board[i][j] == val:
                            return False
            return True
        
        def check_row(self, row: int, col: int, board: List[List[str]]) -> bool:
            val = board[row][col]
            for j in range(len(board[0])):
                if j != col:
                    if board[row][j] == val:
                        return False
            return True

        def check_col(self, row: int, col: int, board: List[List[str]]) -> bool:
            val = board[row][col]
            for i in range(len(board)):
                if i != row:
                    if board[i][col] == val:
                        return False
            return True

        def isValidSudoku(self, board: List[List[str]]) -> bool:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ".": continue
                    if not self.check_box(i, j, board) or not self.check_row(i, j, board) or not self.check_col(i, j, board):
                        return False
            return True
