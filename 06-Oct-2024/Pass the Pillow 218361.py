# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        complete = time//(n-1)
        steps = complete*(n-1)
        if time < n:
            result = time + 1
        elif time > n:
            if complete%2 == 0:
                result = (time-steps)+1
            else:
                result = n - time + steps
        else:
            result =  n-1
        return result