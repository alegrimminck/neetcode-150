# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, maximum):
            nonlocal res
            if not node:
                return
            
            if node.val >= maximum:
                res += 1
                maximum = node.val
            
            dfs(node.left, maximum)
            dfs(node.right, maximum)
        dfs(root, float("-inf"))
        return res