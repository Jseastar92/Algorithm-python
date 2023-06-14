from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        print(root.val)
        # if not root:
            # return root
        
        if root.left :
            root.left = self.invertTree(root.left)
        
        if root.right :
            root.right = self.invertTree(root.right)
        
        root.left, root.right = root.right, root.left
        return root
    
sol = Solution()


# test_case = [1,2,3,4,5]
test_case = [4,2,7,1,3,6,9]

second = TreeNode(2,TreeNode(1,None,None), TreeNode(3,None,None))
sencod2 = TreeNode(7,TreeNode(6,None,None), TreeNode(9,None,None))
root = TreeNode(4, second, sencod2)
sol.invertTree(root)