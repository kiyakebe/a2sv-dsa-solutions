# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True
        
    def checkSimilarity(self, node1, node2):
        if not node1 and not node2:
            return
        if not (node1 and node2):
            self.ans = False
            return

        if node1.val != node2.val:
            self.ans = False
            return

        self.checkSimilarity(node1.left, node2.right)
        self.checkSimilarity(node1.right, node2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.checkSimilarity(root.left, root.right)
        return self.ans
