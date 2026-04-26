from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        @lru_cache
        def dp(row, colm):

            if row >=m:
                return 0
            
            if colm >=n:
                return 0
            if obstacleGrid[row][colm] == 1:
                return 0
            if row == m-1 and colm == n-1:
                return 1
            
            
            
            return dp(row+1, colm) + dp(row, colm+1)
        
        return dp(0,0)


        