# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nums = []
    
    def findNumber(self, node, num):
        if not node:
            return

        num.append(str(node.val))
        if not node.left and not node.right:
            self.nums.append("".join(num[:]))

        if node.left:
            self.findNumber(node.left, num)
        
        if node.right:
            self.findNumber(node.right, num)
        num.pop()

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.findNumber(root, [])
        print(self.nums)
        
        _sum = 0
        for i in self.nums:
            _sum += int(i)

        return _sum
