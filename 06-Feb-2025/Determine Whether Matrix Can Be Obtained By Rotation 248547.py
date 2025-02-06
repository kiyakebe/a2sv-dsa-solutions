# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        track = [True]*4

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                newR = col
                newC = len(mat) - 1 - row
                if mat[newR][newC] != target[row][col]:
                    track[0] = False
                if mat[col][newC] != target[row][col]:
                    track[1] = False
                if mat[newC][len(mat)-1-col] != target[row][col]:
                    track[2] = False
                if mat[len(mat)-1-col][row] != target[row][col]:
                    track[3] = False
                    
        return sum(track) > 0
