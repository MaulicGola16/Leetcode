# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = head
        starting = ending = head
        for i in range(1,k):
            fast = fast.next
        starting = fast
        while fast.next:
            slow = slow.next
            fast = fast.next
        ending = slow
        temp = starting.val
        starting.val = ending.val
        ending.val = temp
        return head