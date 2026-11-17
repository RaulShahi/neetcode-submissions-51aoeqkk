from collections import defaultdict

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return 0

        visited = set()
        graph = defaultdict(list)
        m,n = len(grid), len(grid[0])

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        ans = 0

        def isValid(r,c):
            return 0<=r<m and 0<=c<n and grid[r][c] == 0

        def dfs(r,c):
            if (r,c) == (m-1, n-1):
                return 1
            
            ans = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if isValid(nr,nc) and (nr,nc) not in visited: 
                    visited.add((nr,nc))
                    ans += dfs(nr,nc)
                    visited.remove((nr,nc))
            return ans
        visited.add((0,0))
        return dfs(0,0)


        