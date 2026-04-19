class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            
            if amount in memo:
                return memo[amount]
            
            minm = float("inf")
            for coin in coins:
                minm = min(minm, dp(amount-coin))
            
            memo[amount] = 1+minm
            return memo[amount]
        
        ans = dp(amount)

        return -1 if ans == float("inf") else ans