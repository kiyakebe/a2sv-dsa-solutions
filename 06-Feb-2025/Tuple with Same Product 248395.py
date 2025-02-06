# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        total = 0
        for n in range(len(nums)):
            for m in range(n+1,len(nums)):
                val = nums[n]*nums[m]
                cnt[val]+=1

                if (cnt[val]) > 1:
                    total += (cnt[val]-1)

        return 8*total
