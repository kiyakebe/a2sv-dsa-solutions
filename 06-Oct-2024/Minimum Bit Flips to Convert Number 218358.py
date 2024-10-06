# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cnt = 0
        for i in range(32):
            if start&1<<i != goal&1<<i:
                cnt += 1
        
        return cnt
