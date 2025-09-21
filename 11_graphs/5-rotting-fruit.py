class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        fresh = 0
        rottenFruits = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rottenFruits.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        q = deque(rottenFruits)
        minutes = 0
        while fresh > 0 and q:
            
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = dr+r, dc+c 
                    if (row < 0 or row >= ROWS or
                        col < 0 or col >= COLS or
                        grid[row][col] != 1):
                        continue
                    q.append((row,col))
                    grid[row][col] = 2
                    fresh -= 1
            minutes += 1
        
        return minutes if fresh == 0 else -1
        

        
