# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertNode(self, node, val):
        if node and node.val > val:
            if node.left:
                self.insertNode(node.left, val)
            else:
                new_node = TreeNode(val=val)
                node.left = new_node
                return
        else:
            if node.right:
                self.insertNode(node.right, val)
            else:
                new_node = TreeNode(val=val)
                node.right = new_node
                return

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)

        self.insertNode(root, val)
        
        return root

