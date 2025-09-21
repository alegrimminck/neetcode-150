class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        
        cols = set()
        posDiag = set()
        negDiag = set()
        res = []

        def backtrack(r,c):
            if (c in cols or
                (r+c) in posDiag or
                (c-r) in negDiag):
                return
            
            cols.add(c)
            posDiag.add(r+c)
            negDiag.add(c-r)
            board[r][c] = "Q"
            if r+1 == n:
                res.append(["".join(row) for row in board])
            for col in range(n):
                backtrack(r+1,col)
            cols.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(c-r)
            board[r][c] = "."
        
        for col in range(n):
            backtrack(0, col)
        return res