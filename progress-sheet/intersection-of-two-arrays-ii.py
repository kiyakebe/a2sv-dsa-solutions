class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_freq = dict(Counter(nums1))
        nums2_freq = dict(Counter(nums2))
        ans = []

        for i in nums2_freq:
            if i in nums1_freq:
                ans += [i for _ in range(min(nums1_freq[i], nums2_freq[i]))]
        return ans