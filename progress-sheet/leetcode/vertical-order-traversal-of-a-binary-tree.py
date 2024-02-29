# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self._dict = defaultdict(list)

    def traverse(self, root, x, y):
        if not root:
            return

        self._dict[x].append([y, root.val])
        self.traverse(root.left, x-1, y+1)
        self.traverse(root.right, x+1, y+1)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traverse(root, 0, 0)
        ans = []
        for k in sorted(self._dict.keys()):
            temp = []
            for j in sorted(self._dict[k]):
                temp.append(j[1])
            ans.append(temp)
        
        return ans