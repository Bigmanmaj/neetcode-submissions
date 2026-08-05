# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            cur = head.next
            head.next = None
        else:
            return head
        prev = head
        while cur != None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
    
