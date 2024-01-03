class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        placeholder = 0
        seek = 0
        n = len(nums)
        if(n == 1): return

        while seek < n and placeholder < n:
            if(nums[placeholder] != 0):
                placeholder += 1
                seek = placeholder + 1

            elif(nums[seek] == 0):
                seek += 1
            else:
                nums[seek], nums[placeholder] = nums[placeholder], nums[seek]
                seek = placeholder + 1
