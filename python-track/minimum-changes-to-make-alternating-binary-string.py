class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        operation = 0
        prev = s[0]
        for i in range(1, n):
            if(prev == s[i]):
                operation += 1
                prev = '0' if prev == '1' else '1'
            else:
                prev = s[i]
        return min(operation, n-operation)
