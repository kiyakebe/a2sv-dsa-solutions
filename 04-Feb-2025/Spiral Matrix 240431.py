# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m1, m2 = 0, len(matrix)-1
        n1 ,n2 = 0, len(matrix[0])-1
        x = 0
        ans = []
        
        while m2>=m1 and n2>=n1:
            if x%4 == 0:
                for i in range(n1, n2+1):
                    ans.append(matrix[m1][i])
                m1 += 1
            elif x%4 == 1:
                for i in range(m1, m2+1):
                    ans.append(matrix[i][n2])
                n2 -= 1
            elif x%4 == 2:
                for i in range(n2, n1-1, -1):
                    ans.append(matrix[m2][i])
                m2 -= 1
            else:
                for i in range(m2, m1-1, -1):
                    ans.append(matrix[i][n1])
                n1 += 1
            x += 1
        return ans