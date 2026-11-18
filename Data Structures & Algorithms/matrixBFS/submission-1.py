class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        visited = set()
        def isValid(r,c):
            return 0<=r<ROWS and 0<=c<COLS and grid[r][c] == 0
        queue = deque([(0,0,0)])
        
        while queue:
            r, c, dist = queue.popleft()
            if (r,c) == (ROWS-1, COLS-1):
                return dist
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if isValid(nr,nc) and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc,dist+1)) 

        return -1
        