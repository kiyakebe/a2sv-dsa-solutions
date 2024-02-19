class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0 for i in range(n)]
        st = []
        for i, v in enumerate(temperatures):
            while st and st[-1][1] < v:
                x = st.pop()[0]
                ans[x] = i-x
            st.append((i, v))      
        return ans