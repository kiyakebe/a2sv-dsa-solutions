# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        for i in range(len(arr)):
            prefix_xor.append(prefix_xor[-1]^arr[i])
        ans = []

        for l, r in queries:
            val = prefix_xor[r+1]^prefix_xor[l]
            ans.append(val)
        
        return ans