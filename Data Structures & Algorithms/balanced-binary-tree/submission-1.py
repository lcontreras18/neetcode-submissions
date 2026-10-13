# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #every node is left and right balanced

        balanced = [True]

        def dfs(node):
            if not node:
                return True
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
            
            return 1 + max(left_height, right_height)

        dfs(root)

        return balanced[0]