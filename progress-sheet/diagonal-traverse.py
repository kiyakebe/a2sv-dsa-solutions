class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(deque)
        m = len(mat)
        n = len(mat[0])
        ans = []
        for i in range(m):
            for j in range(n):
                index_sum = i+j
                if index_sum % 2 == 0:
                    d[index_sum].appendleft(mat[i][j])
                else:
                    d[index_sum].append(mat[i][j])
        # the key in the dict are 0 - m+n-1
        for i in range(m+n-1):
            ans += d[i]
            del d[i]
        return ans

# Time Complexity = O(n)
# Space Complexity = O(n)