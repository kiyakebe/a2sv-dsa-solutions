class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pre = [0 for i in range(n)]

        for i in shifts:
            l = i[0]
            r = i[1]
            k = i[2]
            if k == 1:
                pre[l] += 1
                if r+1 < n:
                    pre[r+1] -= 1
            else:
                pre[l] -= 1
                if r+1 < n:
                    pre[r+1] += 1
        for i in range(1, n):
            pre[i] += pre[i-1]
        sl = list(s)

        for i in range(n):
            if pre[i] >= 0:
                sl[i] = chr((ord(sl[i])-97 + pre[i])%26 + 97)
            else:
                n = 26 + (pre[i]%26)
                sl[i] = chr((ord(sl[i])-97 + n)%26 + 97)
        return "".join(sl)