class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        mat = []; temp = []
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                temp.append(strs[j][i])
            mat.append(list(temp))
            temp.clear()
        counter = 0
        for i in mat:
            if i != sorted(i): counter += 1
        return counter
