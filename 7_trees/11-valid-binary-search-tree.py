# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True

        def dfs(node, minimum, maximum):
            nonlocal valid
            if not node:
                return
            
            if not minimum < node.val < maximum:
                valid = False
                return
            
            dfs(node.left, minimum, min(maximum, node.val))
            dfs(node.right, max(minimum, node.val), maximum)
        dfs(root, float("-inf"), float("inf"))
        return valid
