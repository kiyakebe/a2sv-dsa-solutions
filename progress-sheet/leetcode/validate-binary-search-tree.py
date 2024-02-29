# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validateTree(self, node, _min, _max):
        if not node:
            return True

        if not (node.val > _min and node.val < _max):
            return False

        return (self.validateTree(node.left, _min, node.val) and \
                self.validateTree(node.right, node.val, _max)) 

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validateTree(root, float("-inf"), float("inf"))