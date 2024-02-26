class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # make it one indexed
        rowIndex += 1
        row = [1]
        row_curr = [1]

        for i in range(1, rowIndex):
            for j in range(1, len(row)):
                row_curr.append(row[j-1]+row[j])
            row_curr.append(1)
            row = row_curr
            row_curr = [1]
        
        return row
