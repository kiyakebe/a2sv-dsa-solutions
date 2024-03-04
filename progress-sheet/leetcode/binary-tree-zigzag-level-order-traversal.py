# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self._dict = defaultdict(list)

    def dfs(self, node, i):
        if not node:
            return
        
        self.dfs(node.left, i+1)
        self._dict[i].append(node.val)
        self.dfs(node.right, i+1)
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dfs(root, 0)
        ans = []
        for i in sorted(self._dict.keys()):
            if i%2 == 0:
                ans.append(self._dict[i])
            else:
                ans.append(reversed(self._dict[i]))

        return ans