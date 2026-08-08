# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        pos = length - n
        head = ListNode(-1, head)
        cur = head
        counter = 0
        while cur:
            if counter == pos:
                if cur.next:
                    cur.next = cur.next.next
                else:
                    cur.next = None
            counter += 1
            cur = cur.next
        return head.next
        