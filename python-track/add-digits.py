class Solution:
    def addDigits(self, num: int) -> int:

        while num not in range(10):
            l = [int(n) for n in str(num)]
            num = sum(l)
        return num