# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diff = 0

    def findDiff(self, node, _max, _min):
        if not node:
            self.max_diff = max(self.max_diff, abs(_max-_min))
            return
        
        self.findDiff(node.left, max(_max, node.val), min(_min, node.val))
        self.findDiff(node.right, max(_max, node.val), min(_min, node.val))

        
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.findDiff(root, root.val, root.val)
        return self.max_diff