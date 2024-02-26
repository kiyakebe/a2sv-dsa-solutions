class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c=Counter(s)
        chars=set()
        completed=set()

        ans = []
        l = -1
        for i in range(len(s)):
            chars.add(s[i])
            c[s[i]] -= 1
            if c[s[i]]==0:
                completed.add(s[i])
                
            if chars == completed:
                ans.append(i-l)
                l = i
                chars=set()
                completed=set()
        return ans
