class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0 for _ in range(n)]

        dp[0] = 1

        for row in range(m):
            for colm in range(1,n):
                    dp[colm] +=  dp[colm-1]        
        return dp[-1]
        
        #Time - O(m*n)
        #Space - O(m*n)