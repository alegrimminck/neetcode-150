from types import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(closed, opened):
            if closed == opened == n:
                res.append("".join(stack))
                return
            
            if opened < n:
                stack.append("(")
                dfs(closed, opened + 1)
                stack.pop()
            if closed < opened:
                stack.append(")")
                dfs(closed + 1, opened)
                stack.pop()
        
        dfs(0, 0)
        return res
