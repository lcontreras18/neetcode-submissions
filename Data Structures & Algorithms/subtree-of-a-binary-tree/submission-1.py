# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root, subroot):
            if not root and not subroot:
                return True
        
            if (root and not subroot) or (subroot and not root):
                return False
        
            if root.val != subroot.val:
                return False
            
            return(isSameTree(root.left, subroot.left) and isSameTree(root.right, subroot.right))
        
        def sameSubTree(root):
            if not root:
                return False
            
            if isSameTree(root, subRoot):
                return True
            
            return sameSubTree(root.left) or sameSubTree(root.right)

        return sameSubTree(root) 
        
