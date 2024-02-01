# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        before_ln = None
        left_node = head
        
        while count < left:
            count += 1
            before_ln = left_node
            left_node = left_node.next
        b_left_node = left_node
        count = 0
        last_node = None
        # temp = left_node.next
        while count < right-left+1:
            temp = left_node.next
            left_node.next = last_node
            last_node = left_node
            left_node = temp
            count += 1
        b_left_node.next = left_node
        
        if left != 1:
            before_ln.next = last_node 
        else:
            head = last_node

        return head