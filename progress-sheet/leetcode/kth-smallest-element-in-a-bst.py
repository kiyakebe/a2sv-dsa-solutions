# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack = []
        self.count = 0
    def findKth(self, root, k):
        if not root:
            return

        self.findKth(root.left, k)
        self.stack.append(root.val)
        self.findKth(root.right, k)

        if len(self.stack) == k:
            return

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.findKth(root, k)
        return self.stack[k-1]