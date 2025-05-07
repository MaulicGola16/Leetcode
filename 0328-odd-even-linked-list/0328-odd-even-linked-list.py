# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        o, E, e = head, head.next, head.next
        while(o.next and e.next):
            if(o.next.next):
                o.next = o.next.next
                o = o.next
            if e.next.next:
                e.next = e.next.next
                e = e.next
        e.next = None
        o.next = E
        return head