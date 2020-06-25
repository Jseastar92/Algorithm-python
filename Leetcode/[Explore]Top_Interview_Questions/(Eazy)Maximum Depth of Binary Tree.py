# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root :
            return 0
        def searchNode(node: TreeNode, d: int):
            l, r = 0, 0
        
            if not (node.left or node.right):
                return d
            
            if node.left :
                l = searchNode(node.left, d+1)
            
            if node.right :
                r = searchNode(node.right, d+1)

            return l if l > r else r
        
        return searchNode(root, 1)