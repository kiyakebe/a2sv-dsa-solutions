class Solution:
    def isHappy(self, n: int) -> bool:
        def square_sum(n):
            l = list(str(n))
            val = 0
            for i in l:
                val += int(i)**2
            return val
        sl = n
        fs = n
        isStarted = True
        while sl != fs or isStarted:
            isStarted = False
            sl = square_sum(sl)
            fs = square_sum(square_sum(fs))
            if(fs == 1):
                return True
        return False

