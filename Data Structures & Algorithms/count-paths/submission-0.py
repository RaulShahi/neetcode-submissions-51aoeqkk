from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache
        def dp(i,j):
            if i==m-1 and j==n-1:
                return 1
            
            if i >=m :
                return 0
            if j>=n:
                return 0
            return dp(i, j+1) + dp(i+1, j)
        
        return dp(0,0)
        