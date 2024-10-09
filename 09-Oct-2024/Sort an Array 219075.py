# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class MergeSort:
    def __init__(self) -> None:
        pass
    
    def merge(self, left, right):
        merged = []
        ptr1, ptr2 = 0, 0
        
        while ptr1 < len(left) and ptr2 < len(right):
            if left[ptr1] <= right[ptr2]:
                merged.append(left[ptr1])
                ptr1 += 1
            else:
                merged.append(right[ptr2])
                ptr2 += 1
            
        while ptr1 < len(left):
            merged.append(left[ptr1])
            ptr1 += 1
        
        while ptr2 < len(right):
            merged.append(right[ptr2])
            ptr2 += 1
            
        return merged
    
    def merge_sort(self, arr):
        n = len(arr)
        if len(arr) <= 1:
            return arr
        
        mid = n//2
        
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])
        
        return self.merge(left_half, right_half)
    
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mr = MergeSort()
        return mr.merge_sort(nums)