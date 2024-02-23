class Solution:
    def fib(self, n: int) -> int:
        if n < 2: return n
        a = 0
        b = 1
        for i in range(1, n):
            b, a = a+b, b

        return b