# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def good(node, curr_max):
            if not node:
                return 0
            
            if node.val >= curr_max:
                curr_max = node.val
                count = 1
            else:
                count = 0

            count += good(node.left, curr_max)
            count += good(node.right, curr_max)

            return count 

        return good(root, root.val)      