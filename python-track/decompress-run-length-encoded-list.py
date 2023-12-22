class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []; temp =[]
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                temp.append(nums[i+1])
            ans += temp
            temp.clear()
        return ans
        