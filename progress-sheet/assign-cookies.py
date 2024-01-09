class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        counter = 0
        g_ptr = 0
        s_ptr = 0

        while g_ptr < len(g) and s_ptr < len(s):
            g[g_ptr] -= s[s_ptr]
            if g[g_ptr] <= 0:
                g_ptr += 1
                counter += 1
            else:
                g[g_ptr] += s[s_ptr]
            s_ptr += 1

        return counter
        