# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        t = len(typed)

        ptr_n = 0
        ptr_t = 0

        while ptr_n < n:
            char = name[ptr_n]
            count = 0
            while ptr_t < t and typed[ptr_t] == char:
                count += 1
                ptr_t += 1
            
            while ptr_n < n and name[ptr_n] == char:
                count -= 1
                ptr_n += 1
            
            if count < 0:
                return False
            
        if ptr_t != t:
            return False
        return True