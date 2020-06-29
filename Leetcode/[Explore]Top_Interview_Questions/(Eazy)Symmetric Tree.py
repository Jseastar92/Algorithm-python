# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #preOrder
        def travLeft(left, arr=[]):
            arr.append(left.val)
            if left.left:
                travLeft(left.left,arr)
            else:
                arr.append(None)
            if left.right :
                travLeft(left.right, arr)    
            else:
                arr.append(None)
            return arr
        
        #preOrder reversed
        def travRight(right, arr=[]):
            arr.append(right.val)
            if right.right :
                travRight(right.right, arr)
            else:
                arr.append(None)
            if right.left:
                travRight(right.left,arr)
            else:
                arr.append(None)
            return arr
        
        if root:
            if root.left and root.right :
                return travLeft(root.left) == travRight(root.right)
            elif root.left or root.right:
                return False
            else:
                return True
        else :
            return True

'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def core(lt, rt):
            if lt is None and rt is None:
                return True
            if lt is None or rt is None:
                return False
            return lt.val == rt.val and core(lt.right, rt.left) and core(lt.left, rt.right)
        
        
        return core(root, root)
'''