# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.root = TreeNode()

    def buildBST(self, node, nums):
        if not nums:
            return
        
        n = len(nums)
        center = n//2
        node.val = nums[center]
        
        node.left = self.buildBST(TreeNode(), nums[:center])
        node.right = self.buildBST(TreeNode(), nums[center+1:])
        
        return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.buildBST(self.root, nums)
        
        return self.root