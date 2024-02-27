# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = None

    def search(self, root, val):
        if self.ans:
            return
        if not root:
            return
        if root.val == val:
            self.ans = root 

        self.searchBST(root.left, val)
        self.searchBST(root.right, val)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.search(root, val)
        return self.ans