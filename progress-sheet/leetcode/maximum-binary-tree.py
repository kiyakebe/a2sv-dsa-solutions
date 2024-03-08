# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = nums.index(max(nums))
        return TreeNode(nums[mid], self.constructMaximumBinaryTree(nums[:mid]), self.constructMaximumBinaryTree(nums[mid+1:]))