class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans = nums = []
        mid = num//3
        total = 0
        nums.append(mid-1)
        nums.append(mid)
        nums.append(mid+1)
        for i in ans: total += i
        if total == num: return ans
        return []
