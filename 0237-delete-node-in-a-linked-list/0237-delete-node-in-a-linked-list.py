class Solution:
    def deleteNode(self, node: 'ListNode') -> None:
        if not node or not node.next:
            return
        node.val = node.next.val
        node.next = node.next.next