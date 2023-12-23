class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        s += "00"
        ans = ''
        i = 0
        while i < n:
            if(s[i+2] == '#'):
                ans += chr(int(s[i:i+2]) + 96)
                i += 3
            else:
                print(i)
                ans += chr(int(s[i]) + 96)
                i+=1
        print(n)
        return ans