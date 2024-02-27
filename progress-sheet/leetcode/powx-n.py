class Solution:
    def power(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        half_power = self.myPow(x, n//2)

        if n%2 == 1:
            return half_power*half_power*x
        else:
            return half_power*half_power

    def myPow(self, x: float, n: int) -> float:
        val = self.power(x, abs(n))
        if n < 0:
            return 1/val
        else:
            return val