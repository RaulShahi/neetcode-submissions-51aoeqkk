from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        def isValid(r,c):
            return 0<=r<m and 0<=c<n and grid[r][c] == 1
        
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        
        while q and fresh>0:
            cur_len = len(q)

            for _ in range(cur_len):
                r,c = q.popleft()

                for dx, dy in directions:
                    nr, nc =  r+dx, c+dy

                    if isValid(nr,nc):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            time += 1
        
        return time if fresh == 0 else -1


        