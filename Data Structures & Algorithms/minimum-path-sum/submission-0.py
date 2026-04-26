from functools import lru_cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache
        def dp(r, c):
            if r>=m or c>=n:
                return float("inf")
            if r==m-1 and c==n-1:
                return grid[m-1][n-1]
      
            return grid[r][c] + min(dp(r+1,c), dp(r, c+1))
        
        return dp(0,0)



        