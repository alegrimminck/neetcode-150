class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacificStarts = [(i,0) for i in range(1, ROWS)] + [(0,i) for i in range(COLS)]
        atlanticStarts = [(i,COLS-1) for i in range(0, ROWS-1)] + [(ROWS-1,i) for i in range(COLS)]
        
        visitedPacific = [[False]*COLS for _ in range(ROWS)]
        visitedAtlantic = [[False]*COLS for _ in range(ROWS)]

        def dfs(r,c,visited,lastHeight):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                visited[r][c] or lastHeight > heights[r][c]):
                return
            
            visited[r][c] = True
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
        
        for r, c in pacificStarts:
            dfs(r,c,visitedPacific,float("-inf"))
        for r, c in atlanticStarts:
            dfs(r,c,visitedAtlantic,float("-inf"))
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if visitedPacific[r][c] and visitedAtlantic[r][c]:
                    res.append([r,c])
        return res
        