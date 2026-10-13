class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        prev = [float("inf")] * (amount+1)

        prev[0] = 0
        for i in range(n-1, -1, -1):
            curr = [float("inf")] * (amount+1)
            curr[0] = 0
            for j in range(1, amount+1):
                curr[j] = prev[j]

                #take
                if j-coins[i] >= 0:
                    curr[j] = min(curr[j],
                    1+curr[j-coins[i]]
                    )
            prev = curr
      
        
        if prev[amount] == float("inf"):
            return -1
        
        return prev[amount]