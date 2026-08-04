class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, low, high):
            if not node:
                return True
            if node.val > low and node.val < high:
                return validate(node.left, low, node.val) and validate(node.right,node.val, high)
            else:
                return False

        return validate(root, float('-inf'), float('inf'))