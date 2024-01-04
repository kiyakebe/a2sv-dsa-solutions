class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_s = set(nums1)
        for i in nums2:
            if i in nums1_s:
                return i
        return -1