class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less, greater = [], []
        while head:
            if head.val < x:
                less.append(head.val)
            else:
                greater.append(head.val)
            head = head.next
        values = less + greater
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next