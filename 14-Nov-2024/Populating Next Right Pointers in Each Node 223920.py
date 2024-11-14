# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def __init__(self):
        self.levels = {}

    def dfs(self, root, level):
        if not root:
            return
        self.dfs(root.left, level+1)

        if level in self.levels.keys():
            self.levels[level].next = root
        self.levels[level] = root
        
        self.dfs(root.right, level+1)

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.dfs(root, 0)

        return root