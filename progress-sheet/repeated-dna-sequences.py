class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []
        look_up = set()
        ans = set()
        for i in range(10, n+1):
            sub_str = s[i-10:i]
            if sub_str in look_up:
                ans.add(sub_str)
            else:
                look_up.add(sub_str)

        return list(ans)