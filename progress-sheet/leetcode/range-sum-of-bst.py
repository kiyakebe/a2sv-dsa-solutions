# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        v = root.val
        if low <= v <= high:
            self.ans += v
        if root.right:
            self.rangeSumBST(root.right, low, high)
        if root.left:
            self.rangeSumBST(root.left, low, high)
        return self.ans
 