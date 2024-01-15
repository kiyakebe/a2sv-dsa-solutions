class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pc = [0 for i in range(26)]
        sc = [0 for i in range(26)]
        pl = len(p)
        sl = len(s)
        ans = []

        if sl < pl:
            return []

        for i in range(pl):
            pc[ord(p[i])-97] += 1
            sc[ord(s[i])-97] += 1

        if sc == pc:
            ans.append(0)

        for i in range(pl, sl):
            sc[ord(s[i-pl])-97]-=1
            sc[ord(s[i])-97]+=1
            if sc == pc:
                ans.append(i-pl+1)
        return ans