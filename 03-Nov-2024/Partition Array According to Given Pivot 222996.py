# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = [x for x in nums if x < pivot]
        center = [x for x in nums if x ==pivot]
        right = [x for x in nums if x > pivot]
        return left+center+right