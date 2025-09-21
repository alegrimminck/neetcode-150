class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(r,c):
            nonlocal area
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r,c) in visited or
                grid[r][c] == 0):
                return
            
            area += 1
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                area = 0
                if (r,c) not in visited and grid[r][c] == 1:
                    dfs(r,c)
                    maxArea = max(maxArea, area)
        return maxArea