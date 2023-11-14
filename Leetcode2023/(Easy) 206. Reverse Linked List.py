# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node, privious):
            if node is None :
                return privious
            next = node.next
            node.next = privious
            return reverse(next, node)
        return reverse(head, None)