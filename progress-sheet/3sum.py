class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        pairs = set()
        n = len(nums)
        for i in range(n):
            l = i+1
            r = n-1
            while l < r:
                if nums[i] + nums [l] + nums[r] == 0:
                    pairs.add((nums[i], nums [l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[i] + nums [l] + nums[r] < 0:
                    l+=1
                else: r-= 1

        return [[x, y, z] for (x, y, z) in pairs]