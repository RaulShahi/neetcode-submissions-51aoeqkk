class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = [[float("inf")] * (amount+1) for _ in range(n+1)]


        for i in range(n+1):
            memo[i][0] = 0
        print(memo)


        for i in range(n-1, -1, -1):
            for j in range(1, amount+1):
                memo[i][j] = memo[i+1][j]

                #take
                if j-coins[i] >= 0:
                    memo[i][j] = min(memo[i][j],
                    1+memo[i][j-coins[i]]
                    )
      
        
        if memo[0][amount] == float("inf"):
            return -1
        
        return memo[0][amount]