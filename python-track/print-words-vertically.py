class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = []
        max_len = 0
        for i in s.split():
            words.append(list(i))
            max_len = max(max_len, len(i))

        ans = ['' for _ in range(max_len)]
        
        for i in range(max_len):
            for word in words:
                # pass
                if(len(word) > 0):
                    ans[i] += word.pop(0)
                else:
                    ans[i] += " "
                    
        return [word.rstrip(' ') for word in ans]