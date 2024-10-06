# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        _dict = defaultdict(int)
        for i in range(len(arr)):
            val = arr[i]%k
            if _dict[k-val] > 0:
                _dict[k-val] -= 1
            else:
                _dict[val] += 1
        
        if _dict[0]%2 == 0:
            return sum(_dict.values())-_dict[0] == 0
        
        return False