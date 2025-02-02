# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        val = 0
        count = 0
        for i in costs:
            val += i
            if val <= coins:
                count += 1
            else:
                break
                
        return count