class Solution:
    def calc_comb(self, count, freq, mod):
        if freq == 0:
            return 1
        
        half_product = self.calc_comb(count, freq//2, mod)

        if freq%2 == 1:
            return (half_product*half_product*count)%mod
        else:
            return (half_product*half_product)%mod

    def countGoodNumbers(self, n: int) -> int:
        freq = n//2
        max_range = 1000000007
        even = self.calc_comb(5, freq, max_range)
        odd = self.calc_comb(4, freq, max_range)

        if n%2 == 1:
            return (even*odd*5)%max_range
        return (even*odd)%max_range