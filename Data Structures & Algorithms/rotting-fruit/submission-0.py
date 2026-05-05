class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        
        def isValid(r,c):
            return 0<=r<m and 0<=c<n and grid[r][c] == 1
        
        q = deque()
        fresh = 0
        rotten = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    visited.add((i,j))
                    q.append((i,j,0))
                    rotten += 1
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0 and rotten == 0:
            return 0
        
        if rotten == 0:
            return -1
        
        if fresh == 0:
            return 0
        
        while q:
            r, c, steps = q.popleft()

            for dx,dy in directions:
                nr, nc = r +dx, c+dy

                if isValid(nr,nc) and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.append((nr,nc,steps+1))
                    fresh -= 1
        
        return steps if fresh == 0 else -1
        