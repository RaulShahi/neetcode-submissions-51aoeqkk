class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        islands = 0

        visited = set()

        def isValid(r,c):
            return 0<=r<m and 0<=c<n and grid[r][c] == "1"
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        def dfs(r,c):
            for dx, dy in directions:
                nr, nc = r +dx, c + dy
                if (nr,nc) not in visited and isValid(nr,nc):
                    visited.add((nr,nc))
                    dfs(nr,nc)

        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and isValid(i,j):
                    islands += 1
                    visited.add((i,j))
                    dfs(i,j)
        
        return islands

        