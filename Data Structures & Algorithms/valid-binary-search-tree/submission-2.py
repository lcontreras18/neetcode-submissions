# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minimum, maximum):
            if node is None:
                return True

            if node.val >= maximum or node.val <= minimum:
                return False
            
            left = dfs(node.left,minimum,node.val)
            right = dfs(node.right,node.val, maximum)
            
            return right and left
        
        minimum = float('-inf')
        maximum = float('inf')
        return dfs(root, minimum, maximum)

        