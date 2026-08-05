# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        r = res
        l1 = list1
        l2 = list2
        while l1 or l2:
            if not l1:
                r.next = l2
                r = r.next
                break
            if not l2:
                r.next = l1
                r = r.next
                break
            if l1.val >= l2.val:
                r.next = ListNode(l2.val)
                l2 = l2.next
                r = r.next
            else:
                r.next = ListNode(l1.val)
                l1 = l1.next
                r = r.next
        return res.next