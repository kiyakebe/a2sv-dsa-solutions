class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        max_num = 0
        counter = 1
        if(n == 0): return 0
        for i in range(1, n):
            if(nums[i-1]+1 == nums[i]): counter += 1
            elif (nums[i-1] == nums[i]): continue
            else:
                max_num = max(max_num, counter)
                counter = 1
        return max(max_num, counter)

