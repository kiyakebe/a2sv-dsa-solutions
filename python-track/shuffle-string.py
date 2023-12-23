class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ['a' for i in range(len(s))]
        j = 0
        for i in indices:
            ans[i] = s[j]
            j+=1
        return ''.join(ans)
