class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        n = len(nums)
        for i in range(n):
            l = i+1
            r = n-1
            while l < r:
                _sum = nums[i] + nums [l] + nums[r]
                if _sum == target:
                    return target
                elif _sum < target:
                    l+=1
                else: r-= 1
                if abs(_sum - target) < abs(closest - target):
                    closest = _sum
        return closest