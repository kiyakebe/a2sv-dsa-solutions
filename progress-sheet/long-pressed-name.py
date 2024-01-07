class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        if len(name) > len(typed):
            return False

        ptr_n = 0
        ptr_t = 0
        n = len(name)
        t = len(typed)
        
        while ptr_n < n and ptr_t < t:

            char = name[ptr_n]
            count = 0
            print(char)
            while char == name[ptr_n]:
                ptr_n += 1
                count += 1
                if ptr_n == n: break
            while char == typed[ptr_t]:
                ptr_t += 1
                count -= 1
                if ptr_t == t: break
            
            if count > 0:
                return False

        if ptr_n == n and ptr_t == t:
            return True
        else:
            return False