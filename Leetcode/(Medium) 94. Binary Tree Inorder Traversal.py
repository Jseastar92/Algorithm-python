class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        a=[]
        if not root :
            return a
        
        def nodeSearch(tree: TreeNode):
            if not tree.right and not tree.left:
                return a.append(tree.val)
            
            if tree.left:
                nodeSearch(tree.left)
            a.append(tree.val)
            if tree.right:
                nodeSearch(tree.right)

        nodeSearch(root)
            return a