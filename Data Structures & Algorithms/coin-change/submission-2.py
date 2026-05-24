from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        @lru_cache(None)
        def dp(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            
            minm = float("inf")

            for coin in coins:
                minm = min(minm, 1+dp(amount-coin))
            
            return minm
        
        ans = dp(amount)

        return ans if ans != float("inf") else -1
        
        