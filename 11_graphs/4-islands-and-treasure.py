class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,-1), (0,1), (1,0), (-1,0)]
        
        def bfs(r,c):
            q = deque([(r,c)])
            level = 1
            while q:
                l = len(q)
                for _ in range(l):
                    curr = q.popleft()
                    for dr, dc in directions:
                        row, col = curr[0]+dr, curr[1]+dc

                        if (row < 0 or row >= ROWS or
                            col < 0 or col >= COLS or
                            (row,col) in visited or
                            grid[row][col] <= 0 or
                            level > grid[row][col]):
                            continue
                        
                        visited.add((row,col))
                        grid[row][col] = level
                        q.append((row,col))

                level += 1
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited = set()
                    bfs(r,c)

