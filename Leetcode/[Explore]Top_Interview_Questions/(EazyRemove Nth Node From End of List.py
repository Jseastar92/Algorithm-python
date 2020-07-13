# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        if not head :
            return head
        
        def removeNode(head:ListNode, n:int):
            if n == 0:
                head = head.next
                return head
            head.next = removeNode(head.next, n-1)
            return head
        
        def checkingDepth(head:ListNode, d=1):
            if not head.next:
                return d
            d = checkingDepth(head.next, d+1)
            return d
            
        depth = checkingDepth(head)
        index= depth - n
        
        head = removeNode(head, index)
        
        return head