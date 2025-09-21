class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c):
            nonlocal withBorder
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS):
                withBorder = True
                return
            
            if board[r][c] == "X" or (r,c) in visitedWithBorder or (r,c) in visited:
                return
            
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        visitedWithBorder = set()
        for r in range(1, ROWS-1):
            for c in range(1, COLS-1):
                visited = set()
                withBorder = False
                dfs(r,c)

                if withBorder:
                    for value in visited:
                        visitedWithBorder.add(value)
                    continue
                
                for r,c in visited:
                    board[r][c] = "X"

                

