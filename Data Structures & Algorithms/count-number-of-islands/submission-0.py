class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        def isValid(r,c):
            return 0 <= r < m and 0<=c<n and grid[r][c]=="1"
        
        directions = [[-1,0], [1, 0], [0,1], [0,-1]]
        
        seen = set()

        def dfs(r,c):
            for dx,dy in directions:
                nr, nc = r + dx, c+ dy
                if (nr,nc) not in seen and isValid(nr,nc):
                    seen.add((nr,nc))
                    dfs(nr,nc)


        for i in range(m):
            for j in range(n):
                if isValid(i,j) and (i,j) not in seen:
                    ans += 1
                    seen.add((i,j))
                    dfs(i,j)

        return ans
        