# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
    
    def dfs(self, node, depth):
        if node is None or node.val is None :
            return depth
        depth+=1

        return max(self.dfs(node.left, depth), self.dfs(node.right, depth))