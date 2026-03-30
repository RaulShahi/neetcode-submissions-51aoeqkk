class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        seen = set()

        directions = [[0,-1],[0,1],[1,0],[-1,0]]

        def isValid(r,c):
            return 0<=r<m and 0<=c<n and grid[r][c] == 1

        def dfs(r, c):
            total = 1
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if isValid(nr,nc) and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    total += dfs(nr,nc)
            return total

        for i in range(m):
            for j in range(n):
                if isValid(i,j) and (i,j) not in seen:
                    seen.add((i,j))
                    ans = max(ans, dfs(i,j))
        return ans
        