class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1

        for row in range(m):
            for colm in range(n):
                if row > 0:
                    dp[row][colm] += dp[row-1][colm]
                
                if colm >0:
                    dp[row][colm] += dp[row][colm-1]
        
        return dp[m-1][n-1]
        
        