
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS하면서 각 Depth에서 서브트리의 Height 차이를 확인해야함 -> 2이상인경우 균형X
# Height-Balanced Binary Tree

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True
        
        return self.depth(root) >= 0
    
    def depth(self, node: Optional[TreeNode]) -> int:
        if not node :
            return 0
        
        l_depth = self.depth(node.left)
        if l_depth < 0 :
            return -1

        r_depth = self.depth(node.right)
        if r_depth < 0 :
            return -1
        
        if abs(l_depth - r_depth) > 1 :
            return -1

        return max(l_depth, r_depth) + 1
