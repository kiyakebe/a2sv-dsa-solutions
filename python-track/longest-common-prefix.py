class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = len(strs[0])
        end = False
        lcp = 0
        for i in strs:
            min_length = min(min_length, len(i))
        for i in range (min_length):
            c = strs[0][i];
            for s in strs:
                if s[i] != c:
                    end = True
                    break
            if end: break

            lcp += 1
            
            print(lcp, min_length)

        return strs[0][0:lcp]
        
