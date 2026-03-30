from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid),len(grid[0])
        INF = (2**31)-1

        def isValid(r,c):
            return 0<=r<m and 0<=c<n and grid[r][c] != -1
        
        directions = [[0,-1],[0,1],[-1,0], [1,0]]

        seen = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] not in seen and isValid(i,j):
                    if grid[i][j] == 0:
                        seen = set()
                        seen.add((i,j))
                        queue = deque([(i,j)])

                        while queue:
                            r,c = queue.popleft()
                            for dx, dy in directions:
                                nr, nc = r + dx, c + dy

                                if isValid(nr,nc) and (nr,nc) not in seen:
                                    seen.add((nr,nc))
                                    grid[nr][nc] = min(grid[nr][nc], grid[r][c]+1)
                                    queue.append((nr,nc))



        