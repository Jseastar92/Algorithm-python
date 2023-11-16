# Definition for singly-linked list.
from typing import Optional

# 첫번째 풀이. 
# dfs, loop 이용해서.. O(n)
# Two porinter 로 풀어볼것 .
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        depth = self.dfs(0, head)
        target_index = depth//2
        while target_index > 0:
            target_index -= 1
            head = head.next
        return head

def dfs(self, depth, node: Optional[ListNode]):
    depth+=1
    if not node.next:
        return depth
    return self.dfs(depth, node.next)