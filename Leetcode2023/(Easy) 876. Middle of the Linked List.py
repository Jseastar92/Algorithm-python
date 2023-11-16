# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

# 두번째 풀이.
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next        
        return slow

# 첫번째 풀이. 
# loop 이용해서.. O(n)
# Two porinter 로 풀어볼것 .
# def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         depth = self.getDepth(0, head)
#         target_index = depth//2
#         while target_index > 0:
#             target_index -= 1
#             head = head.next
#         return head

# def getDepth(self, depth, node: Optional[ListNode]):
#     depth+=1
#     if not node.next:
#         return depth
#     return self.getDepth(depth, node.next)