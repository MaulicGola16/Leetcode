# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        prev = head
        temp = head.next
        while temp:
            newVal = gcd(prev.val, temp.val)
            newNode = ListNode(newVal, temp)
            prev.next = newNode
            prev = temp
            temp = temp.next
        return head