class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans =[]; temp = []
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            ans.append(list(temp))
            temp.clear()
        return ans