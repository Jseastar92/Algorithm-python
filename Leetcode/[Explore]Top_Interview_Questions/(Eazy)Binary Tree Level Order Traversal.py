# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
First Solution : using max depth search and dictionary
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        def getMaxDepth(root: TreeNode, depth):
            if not root :
                return depth
            
            if not (root.left or root.right):
                return depth
            l, r = 0, 0
            if root.left :
                l = getMaxDepth(root.left, depth+1)
            if root.right :
                r = getMaxDepth(root.right, depth+1)
            
            return l if l > r else r
        
        c = getMaxDepth(root,1)
        print(c)
        dict = {}
        for i in range(c):
            dict[i]=[]
        
        if not root:
            return []
        def getOrderList(root: TreeNode, depth, dict):
            dict[depth].append(root.val)
            if root.left:
                dict = getOrderList(root.left, depth+1, dict)
            
            if root.right:
                dict = getOrderList(root.right, depth+1, dict)
            
            return dict
        
        dict = getOrderList(root,0,dict)
        answer = []
        for i,v in dict.items():
            answer.append(v)
        return answer


'''
Second Solution : using list and index!
'''

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        def getOrderList(root: TreeNode, depth, list1=[]):
            if len(list1) <= depth :
                list1.append([])
            
            list1[depth].append(root.val)
            if root.left:
                list1 = getOrderList(root.left, depth+1, list1)
            
            if root.right:
                list1 = getOrderList(root.right, depth+1, list1)
            
            return list1
        
        answer = getOrderList(root,0)
        return answer
        
        
        