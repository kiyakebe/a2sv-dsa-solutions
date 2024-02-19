class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        st = []
        for i in nums2:
            while st and st[-1] < i:
                d[st.pop()] = i

            st.append(i)
        
        for i in range(len(nums1)):
            if nums1[i] in d:
                nums1[i] = d[nums1[i]]
            else:
                nums1[i] = -1
        return nums1