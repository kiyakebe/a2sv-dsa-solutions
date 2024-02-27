# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.counter = defaultdict(int)

    def count(self, root: Optional[TreeNode]):
        if not root:
            return
        self.counter[root.val] += 1
        self.count(root.left)
        self.count(root.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.count(root)

        max_count = float("-inf")
        values = []

        for k, v in self.counter.items():
            if v > max_count:
                max_count = v
                values = []
            
            if v == max_count:
                values.append(k)

        return values