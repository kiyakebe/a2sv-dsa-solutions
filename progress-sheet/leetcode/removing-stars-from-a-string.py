class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        n = len(s)
        for i in s:
            if i == '*':
                st.pop()
            else:
                st.append(i)
        
        return "".join(st)