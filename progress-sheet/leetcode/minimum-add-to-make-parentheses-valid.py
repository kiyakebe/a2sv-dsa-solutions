class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        for i in s:
            if i == '(':
                st.append('(')
            elif i == ')':
                if st and st[-1] == '(':
                    st.pop()
                else:
                    st.append(')')
        return len(st)