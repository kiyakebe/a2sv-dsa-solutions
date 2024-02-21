class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vo = {'+', '-', '*', '/'}
        st = []

        for i in tokens:
            if i in vo:
                x = st.pop()
                y = st.pop()
                if i == '*':
                    st.append(y*x)
                elif i == '/':
                    st.append(int(y/x))
                elif i == '+':
                    st.append(y+x)
                else:
                    st.append(y-x)
            else:
                st.append(int(i))
        return st[0]