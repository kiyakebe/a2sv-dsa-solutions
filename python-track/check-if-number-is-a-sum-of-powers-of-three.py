class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        rem = 0
        while n>1:
            if n%3 == 0 or n%3 == 1:
                n = n//3
            else:
                return False
        else:
            return True        
