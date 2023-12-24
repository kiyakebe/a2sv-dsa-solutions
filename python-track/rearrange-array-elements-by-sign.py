class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        # looking_for = 1-> searching for positive
        # looking_for = 0-> searching for negetive
        nv_pointer = 0
        pv_pointer = 0
        looking_for = 1
        while len(ans) != len(nums):
            if(looking_for):
                if(nums[pv_pointer] > 0):
                    ans.append(nums[pv_pointer])
                    looking_for = 0
                pv_pointer += 1
            else:
                if(nums[nv_pointer] < 0):
                    ans.append(nums[nv_pointer])
                    looking_for = 1
                nv_pointer += 1
        return ans