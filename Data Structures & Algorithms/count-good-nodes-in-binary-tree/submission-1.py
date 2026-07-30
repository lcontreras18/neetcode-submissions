# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        node = root
        maxValue = node.val

        def good(node, maximum):
            if not node:
                return 0
            if node.val >= maximum:
                maximum = node.val
                return 1 + good(node.left, maximum) + good(node.right,maximum)
            else:
                return 0 + good(node.left, maximum) + good(node.right,maximum)
        
        if node:
            return good(node, maxValue)

        