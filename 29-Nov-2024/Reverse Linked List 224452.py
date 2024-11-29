# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.new_head = ListNode(1000000)
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        new_node = ListNode(head.val)
        if self.new_head:
            new_head = new_node
        else:
            new_node.next = self.new_head
            self.new_head = new_node
        print(1)
        self.reverseList(head.next)
        
        return self.new_head