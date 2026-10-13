# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def good(node, greatest):
            nonlocal count

            if not node:
                return
            
            if node.val >= greatest:
                count += 1
                greatest = node.val
            
            good(node.left, greatest)
            good(node.right, greatest)
            
        good(root, root.val)

        return count



        